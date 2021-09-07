#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl.UTF-8):	Przeglądarka zasobów SMB
Name:		smb4k
Version:	3.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/smb4k/Development/%{name}-%{version}.tar.xz
# Source0-md5:	85e7c8432eece913086ab982c0555555
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
BuildRequires:	ninja
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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%{?with_tests:%ninja_build test}

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

#fixing desktop file
%{__sed} -e "s@Categories=Qt;KDE;Utility;@Categories=Qt;KDE;Network;@g" -i $RPM_BUILD_ROOT%{_desktopdir}/org.kde.smb4k.desktop

%find_lang %{name} --with-kde --all-name

#%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmb4kcore.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README
%attr(755,root,root) %{_bindir}/smb4k
%attr(755,root,root) %{_libdir}/libsmb4kcore.so
#%attr(755,root,root) %ghost %{_libdir}/libsmb4kcore.so.6
%attr(755,root,root) %{_libdir}/qt5/plugins/smb4kconfigdialog.so
%dir %attr(755,root,root) %{_libdir}/qt5/qml/org/kde/smb4k
%dir %attr(755,root,root) %{_libdir}/qt5/qml/org/kde/smb4k/smb4kqmlplugin
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/smb4k/smb4kqmlplugin/libsmb4kqmlplugin.so
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/smb4k/smb4kqmlplugin/qmldir
%attr(755,root,root) %{_libexecdir}/kauth/mounthelper
%{_desktopdir}/org.kde.smb4k.desktop
%{_datadir}/dbus-1/system-services/org.kde.smb4k.mounthelper.service
%{_datadir}/dbus-1/system.d/org.kde.smb4k.mounthelper.conf
%{_datadir}/kconf_update/*

%{_datadir}/metainfo/org.kde.smb4k.appdata.xml
%{_datadir}/metainfo/org.kde.smb4kqml.appdata.xml

%{_docdir}/HTML/*/smb4k

%{_datadir}/knotifications5/smb4k.notifyrc
#%{_datadir}/kservices5/plasma-applet-org.kde.smb4kqml.desktop
%dir %{_datadir}/kxmlgui5
%dir %{_datadir}/kxmlgui5/smb4k
%{_datadir}/kxmlgui5/smb4k/smb4k_shell.rc
        
%{_datadir}/config.kcfg/smb4k.kcfg
%{_iconsdir}/*/*/*/*.png

%dir %{_datadir}/plasma/plasmoids/org.kde.smb4kqml
%dir %{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/config
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/BookmarkItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/BookmarksPage.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/ConfigurationPage.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/NetworkBrowserItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/NetworkBrowserPage.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/PanelIconWidget.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/PopupDialog.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/ProfileItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/ProfilesPage.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/SharesViewItemDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/SharesViewPage.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/metadata.json

%{_datadir}/polkit-1/actions/org.kde.smb4k.mounthelper.policy
