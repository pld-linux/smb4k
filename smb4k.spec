Summary:       SMB Share Browser
Name:          smb4k
Version:       0.3.2
Release:       1
Distribution:  Fedora Core 1
License:       GPL
Group:         Applications/Internet
Vendor:        Alexander Reinholdt <dustpuppy@mail.berlios.de>
Packager:      Marcin Garski <garski@poczta.onet.pl>
URL:           http://smb4k.berlios.de/
Source:        http://download.berlios.de/smb4k/%{name}-%{version}.tar.gz
BuildRequires: kdelibs-devel >= 3.1.0
BuildRequires: qt-devel >= 3.1.1
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
An SMB share browser for KDE.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/applnk/Applications/%{name}.desktop %{buildroot}%{_datadir}/applications
rm -rf %{buildroot}%{_datadir}/applnk

%clean
rm -rf %{buildroot} %{_builddir}/%{name}-%{version}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING README TODO
%{_bindir}/smb4k
%{_datadir}/applications/smb4k.desktop
%{_datadir}/apps/smb4k/smb4kui.rc
%{_datadir}/doc/*
%{_datadir}/icons/crystalsvg/*
%{_datadir}/locale/*

%changelog
* Wed Jan 21 2004 Marcin Garski <garski@poczta.onet.pl> 0.3.2-1
- Rebuild for Fedora Core 1
* Thu Dec 18 2003 Marcin Garski <garski@poczta.onet.pl> 0.3.1-3
- Cleanup specfile
* Fri Nov 27 2003 Marcin Garski <garski@poczta.onet.pl> 0.3.1-2
- First specfile based on specfile by Ian Geiser <geiseri@msoe.edu>
