%include perl-header-unstable.spec

Summary: Determine the locale encoding.

%define module_name Encode-Locale

Name: perl-module-%{module_name}
Version: 1.02
Release: 1.ru
Group: System Environment/Base
License: GPL/Artistic
Source: %{module_name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl
Requires: perl-module-Encode-Alias

%description
In many applications it's wise to let Perl use Unicode for the strings it processes. Most of the interfaces Perl has to the outside world is still byte based. Programs therefore needs to decode byte strings that enter the program from the outside and encode them again on the way out.

The POSIX locale system is used to specify both the language conventions requested by the user and the preferred character set to consume and output. The Encode::Locale module looks up the charset and encoding (called a CODESET in the locale jargon) and arrange for the Encode module to know this encoding under the name "locale". It means bytes obtained from the environment can be converted to Unicode strings by calling Encode::encode(locale => $bytes) and converted back again with Encode::decode(locale => $string).

Where file systems interfaces pass file names in and out of the program we also need care. The trend is for operating systems to use a fixed file encoding that don't actually depend on the locale; and this module determines the most appropriate encoding for file names. The Encode module will know this encoding under the name "locale_fs". For traditional Unix systems this will be an alias to the same encoding as "locale".

For programs running in a terminal window (called a "Console" on some systems) the "locale" encoding is usually a good choice for what to expect as input and output. Some systems allows us to query the encoding set for the terminal and Encode::Locale will do that if available and make these encodings known under the Encode aliases "console_in" and "console_out". For systems where we can't determine the terminal encoding these will be aliased as the same encoding as "locale". The advice is to use "console_in" for input known to come from the terminal and "console_out" for output known to go from the terminal.

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
find $RPM_BUILD_ROOT -name .packlist | xargs rm
find $RPM_BUILD_ROOT -name perllocal.pod | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT



%files
%defattr(-,bin,bin)
%doc Changes MANIFEST
%{site_perl}/Encode/Locale.pm

%changelog
* Fri Mar 31 2011 Vaibhav Verma <vverna@nbcs.rutgers.edu> 1.02-1.ru
- Initial Rutgers build
