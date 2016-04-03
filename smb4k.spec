#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl.UTF-8):	Przeglądarka zasobów SMB
Name:		smb4k
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz
# Source0-md5:	19043c4c13a7e552e6d30f26dc750089
URL:		http://smb4k.sf.net
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libxml2-progs
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	cups-backend-smb
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An SMB share browser for KDE.

%description -l pl.UTF-8
Przeglądarka zasobów SMB dla KDE.

%prep
%setup -q

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#fixing desktop file
%{__sed} -e "s@Categories=Qt;KDE;Utility;@Categories=Qt;KDE;Network;@g" -i $RPM_BUILD_ROOT%{_desktopdir}/kde4/%{name}.desktop

%find_lang %{name} --with-kde
%find_lang %{name}-core --with-kde
cat %{name}-core.lang >> %{name}.lang
%find_lang plasma_applet_smb4k-qml --with-kde
cat plasma_applet_smb4k-qml.lang >> %{name}.lang

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/lib{smb4kconfigdialog,smb4kcore}.so
rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README
%attr(755,root,root) %{_bindir}/smb4k
%attr(755,root,root) %{_libdir}/libsmb4kcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmb4kcore.so.4
%attr(755,root,root) %{_libdir}/libsmb4ktooltips.so
%attr(755,root,root) %{_libdir}/kde4/*.so
%attr(755,root,root) %{_libdir}/kde4/libexec/mounthelper
# *.la are required
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/net.sourceforge.smb4k.mounthelper.conf
%{_datadir}/apps/kconf_update/*
%{_datadir}/dbus-1/system-services/net.sourceforge.smb4k.mounthelper.service
%{_datadir}/polkit-1/actions/net.sourceforge.smb4k.mounthelper.policy
%{_datadir}/apps/smb4k
%{_datadir}/config.kcfg/smb4k.kcfg
%{_datadir}/appdata/smb4k.appdata.xml
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde4/%{name}.desktop
# plasma applet - maybe could be put in external package?
%{_datadir}/kde4/services/plasma-applet-smb4k-qml.desktop
%{_datadir}/apps/plasma/plasmoids/smb4k-qml
