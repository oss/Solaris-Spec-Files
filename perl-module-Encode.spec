%include perl-header-unstable.spec

Summary: character encodings

%define module_name Encode

Name: perl-module-%{module_name}
Version: 2.42
Release: 1.ru
Group: System Environment/Base
License: GPL/Artistic
Source: %{module_name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl >= 5.7.1
BuildRequires: perl-devel >= 5.7.1
Provides: perl-module-Encode-Alias
Provides: perl-module-Encode-Encoding
Provides: perl-module-Encode-Supported
Provides: perl-module-Encode-CN
Provides: perl-module-Encode-JP
Provides: perl-module-Encode-KR
Provides: perl-module-Encode-TW

%description
The Encode module provides the interfaces between Perl's strings and the rest of the system. Perl strings are sequences of characters.

The repertoire of characters that Perl can represent is at least that defined by the Unicode Consortium. On most platforms the ordinal values of the characters (as returned by ord(ch)) is the "Unicode codepoint" for the character (the exceptions are those platforms where the legacy encoding is some variant of EBCDIC rather than a super-set of ASCII - see perlebcdic).

Traditionally, computer data has been moved around in 8-bit chunks often called "bytes". These chunks are also known as "octets" in networking standards. Perl is widely used to manipulate data of many types - not only strings of characters representing human or computer languages but also "binary" data being the machine's representation of numbers, pixels in an image - or just about anything.

When Perl is processing "binary data", the programmer wants Perl to process "sequences of bytes". This is not a problem for Perl - as a byte has 256 possible values, it easily fits in Perl's much larger "logical character".

%prep

%setup -q -n %{module_name}-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

#Remove the packlist file
#rm -f /usr/perl5/site_perl/%{perl_version}/%{perl_arch}/auto/REST/Google/Apps/EmailSettings/.packlist
find $RPM_BUILD_ROOT -name .packlist | xargs rm
find $RPM_BUILD_ROOT -name *.pod | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,bin,bin)
%doc README Changes

%{global_perl_arch}/Encode.pm
%{global_perl_arch}/Encode/Alias.pm
%{global_perl_arch}/Encode/Byte.pm
%{global_perl_arch}/Encode/CJKConstants.pm
%{global_perl_arch}/Encode/CN.pm
%{global_perl_arch}/Encode/CN/HZ.pm
%{global_perl_arch}/Encode/Changes.e2x
%{global_perl_arch}/Encode/Config.pm
%{global_perl_arch}/Encode/ConfigLocal_PM.e2x
%{global_perl_arch}/Encode/EBCDIC.pm
%{global_perl_arch}/Encode/Encoder.pm
%{global_perl_arch}/Encode/Encoding.pm
%{global_perl_arch}/Encode/GSM0338.pm
%{global_perl_arch}/Encode/Guess.pm
%{global_perl_arch}/Encode/JP.pm
%{global_perl_arch}/Encode/JP/H2Z.pm
%{global_perl_arch}/Encode/JP/JIS7.pm
%{global_perl_arch}/Encode/KR.pm
%{global_perl_arch}/Encode/KR/2022_KR.pm
%{global_perl_arch}/Encode/MIME/Header.pm
%{global_perl_arch}/Encode/MIME/Header/ISO_2022_JP.pm
%{global_perl_arch}/Encode/MIME/Name.pm
%{global_perl_arch}/Encode/Makefile_PL.e2x
%{global_perl_arch}/Encode/README.e2x
%{global_perl_arch}/Encode/Symbol.pm
%{global_perl_arch}/Encode/TW.pm
%{global_perl_arch}/Encode/Unicode.pm
%{global_perl_arch}/Encode/Unicode/UTF7.pm
%{global_perl_arch}/Encode/_PM.e2x
%{global_perl_arch}/Encode/_T.e2x
%{global_perl_arch}/Encode/encode.h
%{global_perl_arch}/auto/Encode/Byte/Byte.bs
%{global_perl_arch}/auto/Encode/Byte/Byte.so
%{global_perl_arch}/auto/Encode/CN/CN.bs
%{global_perl_arch}/auto/Encode/CN/CN.so
%{global_perl_arch}/auto/Encode/EBCDIC/EBCDIC.bs
%{global_perl_arch}/auto/Encode/EBCDIC/EBCDIC.so
%{global_perl_arch}/auto/Encode/Encode.bs
%{global_perl_arch}/auto/Encode/Encode.so
%{global_perl_arch}/auto/Encode/JP/JP.bs
%{global_perl_arch}/auto/Encode/JP/JP.so
%{global_perl_arch}/auto/Encode/KR/KR.bs
%{global_perl_arch}/auto/Encode/KR/KR.so
%{global_perl_arch}/auto/Encode/Symbol/Symbol.bs
%{global_perl_arch}/auto/Encode/Symbol/Symbol.so
%{global_perl_arch}/auto/Encode/TW/TW.bs
%{global_perl_arch}/auto/Encode/TW/TW.so
%{global_perl_arch}/auto/Encode/Unicode/Unicode.bs

%{global_perl_arch}/auto/Encode/Unicode/Unicode.so
%{global_perl_arch}/encoding.pm
%{perl_prefix}/bin/enc2xs
%{perl_prefix}/bin/piconv
%{perl_prefix}/man/man1/enc2xs.1
%{perl_prefix}/man/man1/piconv.1

%{perl_prefix}/man/man3/*


%changelog
* Fri Mar 31 2011 Vaibhav Verma <vverna@nbcs.rutgers.edu> 2.42-1.ru 
- Initial Rutgers build
