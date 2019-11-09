#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl.UTF-8):	Przeglądarka zasobów SMB
Name:		smb4k
Version:	3.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz
# Source0-md5:	12ea7b57edec04e74276ecc7a37801f5
URL:		http://smb4k.sf.net
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	docbook-dtd45-xml
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libxml2-progs
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
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
mkdir -p build
cd build
%cmake ../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#fixing desktop file
%{__sed} -e "s@Categories=Qt;KDE;Utility;@Categories=Qt;KDE;Network;@g" -i $RPM_BUILD_ROOT%{_desktopdir}/org.kde.smb4k.desktop

%find_lang %{name} --with-kde --all-name

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmb4kcore.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README
%{_docdir}/HTML/en
%attr(755,root,root) %{_bindir}/smb4k
%attr(755,root,root) %{_libdir}/libsmb4kcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmb4kcore.so.6
%attr(755,root,root) %{_libdir}/plugins/smb4kconfigdialog.so
%attr(755,root,root) %{_libexecdir}/kauth/mounthelper
%attr(755,root,root) %{_datadir}/kconf_update/*.sh
%{_datadir}/kconf_update/*.upd
%{_datadir}/dbus-1/system-services/org.kde.smb4k.mounthelper.service
%{_datadir}/dbus-1/system.d/org.kde.smb4k.mounthelper.conf
%{_datadir}/polkit-1/actions/org.kde.smb4k.mounthelper.policy
#%{_datadir}/apps/smb4k
%{_datadir}/config.kcfg/smb4k.kcfg
%{_datadir}/metainfo/org.kde.smb4k.appdata.xml
%{_datadir}/metainfo/org.kde.smb4kqml.appdata.xml
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/org.kde.smb4k.desktop
# plasma applet - maybe could be put in external package?
%attr(755,root,root) %{_libdir}/qml/org/kde/smb4k/smb4kqmlplugin/libsmb4kqmlplugin.so
%{_libdir}/qml/org/kde/smb4k/smb4kqmlplugin/qmldir
%{_datadir}/knotifications5/smb4k.notifyrc
%{_datadir}/kservices5/plasma-applet-org.kde.smb4kqml.desktop
%{_datadir}/kxmlgui5/smb4k/smb4k_shell.rc
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml
