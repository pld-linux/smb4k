#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl.UTF-8):	Przeglądarka zasobów SMB
Name:		smb4k
Version:	4.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/smb4k/Development/%{name}-%{version}.tar.xz
# Source0-md5:	5c426e1b1ae58f6dbc7a18da59440c2b
URL:		http://smb4k.sf.net
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Keychain-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	docbook-dtd45-xml
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kcompletion-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcrash-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kdnssd-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	kf6-kguiaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kiconthemes-devel
BuildRequires:	kf6-kio-devel
BuildRequires:	kf6-kjobwidgets-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-kstatusnotifieritem-devel
BuildRequires:	kf6-kwallet-devel
BuildRequires:	kf6-kwindowsystem-devel
BuildRequires:	kp6-libplasma-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libxml2-progs
BuildRequires:	ninja
BuildRequires:	qt6-build
BuildRequires:	qt6-qmake
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
%doc AUTHORS BUGS ChangeLog
%attr(755,root,root) %{_bindir}/smb4k
%attr(755,root,root) %{_libdir}/libsmb4kcore.so
%attr(755,root,root) %{_libdir}/libsmb4kdialogs.so
#%attr(755,root,root) %ghost %{_libdir}/libsmb4kcore.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/smb4kconfigdialog.so
%dir %attr(755,root,root) %{_libdir}/qt6/qml/org/kde/smb4k
%dir %attr(755,root,root) %{_libdir}/qt6/qml/org/kde/smb4k/smb4kqmlplugin
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/smb4k/smb4kqmlplugin/libsmb4kqmlplugin.so
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/smb4k/smb4kqmlplugin/qmldir
%attr(755,root,root) %{_libexecdir}/kf6/kauth/mounthelper
%{_desktopdir}/org.kde.smb4k.desktop
%{_datadir}/dbus-1/system-services/org.kde.smb4k.mounthelper.service
%{_datadir}/dbus-1/system.d/org.kde.smb4k.mounthelper.conf
#%{_datadir}/kconf_update/*

%{_datadir}/metainfo/org.kde.smb4k.appdata.xml
%{_datadir}/metainfo/org.kde.smb4kqml.appdata.xml

%{_docdir}/HTML/*/smb4k

%{_datadir}/knotifications6/smb4k.notifyrc
        
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
%{_datadir}/plasma/plasmoids/org.kde.smb4kqml/metadata.json

%{_datadir}/polkit-1/actions/org.kde.smb4k.mounthelper.policy
