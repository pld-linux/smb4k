#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl.UTF-8):	Przeglądarka zasobów SMB
Name:		smb4k
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
# Source0-md5:	49d7a58f751d04c6c0697ee5e5912d4d
URL:		http://smb4k.berlios.de/
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-Makefile.patch
Patch2:		kde-ac260-lt.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.2
BuildRequires:	qt-devel >= 6:3.2
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	cups-backend-smb
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An SMB share browser for KDE.

%description -l pl.UTF-8
Przeglądarka zasobów SMB dla KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.* admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#fixing desktop file
%{__sed} -e "s@Categories=Qt;KDE;Utility;@Categories=Qt;KDE;Network;@g" -i $RPM_BUILD_ROOT%{_desktopdir}/kde/%{name}.desktop

%find_lang %{name} --with-kde

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

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
%attr(755,root,root) %{_bindir}/smb4k_cat
%attr(755,root,root) %{_bindir}/smb4k_mv 
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
# *.la are required
%{_libdir}/kde3/*.la
%{_datadir}/apps/smb4k
%{_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{_iconsdir}/crystalsvg/*/apps/*.png
%{_desktopdir}/kde/%{name}.desktop
