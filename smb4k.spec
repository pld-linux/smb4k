TODO: desktop file
Summary:	SMB Share Browser
Summary(pl):	Przegl±darka zasobów SMB
Name:		smb4k
Version:	0.3.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
URL:		http://smb4k.berlios.de/
Source0:	http://download.berlios.de/smb4k/%{name}-%{version}.tar.gz
# Source0-md5:	081e345032171389d409f66412515e7c
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1.0
BuildRequires:	qt-devel >= 3.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An SMB share browser for KDE.

%description -l pl
Przegl±darka zasobów SMB dla KDE.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install -D $RPM_BUILD_ROOT%{_datadir}/applnapplications
#mv %{buildroot}%{_datadir}/applnk/Applications/%{name}.desktop %{buildroot}%{_datadir}/applications
#rm -rf %{buildroot}%{_datadir}/applnk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog COPYING README TODO
%attr(755,root,root) %{_bindir}/smb4k
#%{_datadir}/applications/smb4k.desktop
%{_datadir}/apps/smb4k/smb4kui.rc
%{_datadir}/doc/*
%{_datadir}/icons/crystalsvg/*
%{_datadir}/locale/*
