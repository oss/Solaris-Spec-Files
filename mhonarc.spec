
%define name MHonArc
%define version 2.6.16
%define release 2
%define prefix /usr/local

Name:		%{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl mail-to-HTML converter
Group:          Applications/Internet
License:        GPL
URL:            http://www.mhonarc.org/
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
Distribution:   RU-Solaris
Vendor:         NBCS-OSS
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Provides:       %{name} = %{version}-%{release}
Requires:	perl
BuildRequires:	perl

%description
MHonArc is a Perl mail-to-HTML converter. MHonArc provides HTML mail
archiving with index, mail thread linking, etc; plus other
capabilities including support for MIME and powerful user
customization features.


%prep
%setup -q 

#%build

%install
rm -rf $RPM_BUILD_ROOT

%{__perl} install.me \
	-batch \
	-prefix %{_prefix} \
	-libpath $RPM_BUILD_ROOT%{_datadir}/mhonarc \
	-manpath $RPM_BUILD_ROOT%{_mandir} \
	-binpath $RPM_BUILD_ROOT%{_bindir} \
	-docpath $RPM_BUILD_ROOT%{_docdir}

# Aww, remainders of buildroot and /usr/local, weed 'em out.
%{__perl} -pi -e \
  "s|$RPM_BUILD_ROOT\b||g ; s|/usr/local/bin/perl\b|%{__perl}|g" \
  $RPM_BUILD_ROOT%{_bindir}/* examples/mha*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ACKNOWLG BUGS CHANGES COPYING RELNOTES TODO
%doc doc examples extras logo

%{_bindir}
%{_docdir}
%{_mandir}
%{_datadir}/mhonarc

%changelog
* Fri May 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 2.6.16-2
- Fixing some path issues
* Fri May 11 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> 2.6.16-1
- Initial Build.

