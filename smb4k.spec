#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl.UTF-8):	Przeglądarka zasobów SMB
Name:		smb4k
Version:	0.10.1
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
# Source0-md5:	6488ca6070d12cd6f87dc7088434167d
URL:		http://smb4k.berlios.de/
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-devel
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

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/lib{smb4kconfigdialog,smb4kcore}.so
rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/smb4k
%attr(755,root,root) %{_bindir}/smb4k_kill
%attr(755,root,root) %{_bindir}/smb4k_mount
%attr(755,root,root) %{_bindir}/smb4k_umount
%attr(755,root,root) %{_bindir}/smb4k_sudowriter
%attr(755,root,root) %{_libdir}/libsmb4kcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmb4kcore.so.3
%attr(755,root,root) %{_libdir}/libsmb4kdialogs.so
%attr(755,root,root) %{_libdir}/kde4/*.so
# *.la are required
%{_datadir}/apps/smb4k
%attr(755,root,root) %{_datadir}/apps/kconf_update/authentication1.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/network1.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/network2.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/samba1.sh
%attr(755,root,root) %{_datadir}/apps/kconf_update/smb4ksettings.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/userinterface1.sh
%{_datadir}/config.kcfg/smb4k.kcfg
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde4/%{name}.desktop
