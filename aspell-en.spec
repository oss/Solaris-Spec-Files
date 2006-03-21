Name: aspell-en
Summary: aspell en dictionaries
Version: 0.60.4
Release: 2
Copyright: GPL
Group: Applications/Spelling
Source: ftp://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-6.0-0.tar.bz2
URL: http://aspell.net/
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Jonathan Kaczynski <jmkacz@oss.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: aspell
BuildRequires: aspell

%description
This package contains the following en dictionaries:
en-variant_0 (english-variant_0)
en-variant_1 (english-variant_1)
en-variant_2 (english-variant_2)
en-w_accents (english-w_accents)
en-wo_accents (en english english-wo_accents)
en_CA-w_accents (canadian-w_accents)
en_CA-wo_accents (canadian canadian-wo_accents en_CA)
en_GB-ise-w_accents (british-ise-w_accents british-w_accents
                     en_GB-w_accents)
en_GB-ise-wo_accents (british british-ise british-ise-wo_accents
                      british-wo_accents en_GB en_GB-ise
                      en_GB-wo_accents)
en_GB-ize-w_accents (british-ize-w_accents)
en_GB-ize-wo_accents (british-ize british-ize-wo_accents en_GB-ize)
en_US-w_accents (american-w_accents)
en_US-wo_accents (american american-wo_accents en_US)

%prep
%setup -q -n aspell6-en-6.0-0

%build
./configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,other)
%doc README README.iso Copyright info doc/
/usr/local/lib/aspell-0.60/*

%changelog
* Mon Mar 20 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> 0.60.4-1
- Initial package