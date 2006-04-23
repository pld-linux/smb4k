#
#Note: smb4k needs suid root on smbmnt and smbumount
#
Summary:	SMB share browser
Summary(pl):	Przegl±darka zasobów SMB
Name:		smb4k
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://download.berlios.de/smb4k/%{name}-%{version}.tar.bz2
# Source0-md5:	a221dd7f4e206799ea52d8a249d1a2b5
URL:		http://smb4k.berlios.de/
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-desktop.patch
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 9:3.1.0
BuildRequires:	qt-devel >= 3.1.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	cups-backend-smb
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An SMB share browser for KDE.

%description -l pl
Przegl±darka zasobów SMB dla KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.* admin

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

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
