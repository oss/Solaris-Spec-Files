%include perl-header.spec

Summary: RT modules -- All of Request Tracker's required perl modules

Name: perl-module-RT-modules
Version: 3.0.4
Release: 4
Group: System Environment/Base
Copyright: GPL/Artistic
Requires: perl
%if %{which_perl} == "REPOSITORY"
Requires: perl-module-ExtUtils-MakeMaker >= 6.05-1
BuildRequires: perl-module-ExtUtils-MakeMaker >= 6.05-1
%endif
Requires: perl-module-Module-Build >= 0.18-1 
Requires: perl-module-Digest-MD5
Requires: perl-module-DBI
Requires: perl-module-Apache-DBI
Requires: perl-module-Test-Inline
Requires: perl-module-Class-ReturnValue
Requires: perl-module-DBIx-SearchBuilder
Requires: perl-module-Text-Template
Requires: perl-module-Text-Iconv
Requires: perl-module-File-Spec
Requires: perl-module-Log-Dispatch
Requires: perl-module-Locale-Maketext
Requires: perl-module-Locale-Maketext-Lexicon
Requires: perl-module-Locale-Maketext-Fuzzy
Requires: perl-module-Text-Wrapper
Requires: perl-module-TermReadKey
Requires: perl-module-Text-Autoformat
Requires: perl-module-Text-Quoted
Requires: perl-module-Params-Validate
Requires: perl-module-Cache-Cache
Requires: perl-module-Exception-Class
Requires: perl-module-HTML-Mason
Requires: perl-module-MLDBM
Requires: perl-module-Errno
Requires: perl-module-Freeze-Thaw
Requires: perl-module-Apache-Session
Requires: perl-module-HTML-Tree
Requires: perl-module-HTML-Format
Requires: perl-module-libwww
Requires: perl-module-Regexp-Common
Requires: perl-module-Time-HiRes
Requires: perl-module-TimeDate
Requires: perl-module-Test-Inline
Requires: perl-module-WWW-Mechanize
Requires: perl-module-libapreq
Requires: perl-module-DBI
Requires: perl-module-DBD-mysql
Requires: perl-module-HTML-Parser
Requires: perl-module-File-Temp
Requires: perl-module-Storable
Requires: perl-module-libnet
Requires: perl-module-MIME-tools
Requires: perl-module-MailTools
Requires: perl-module-libnet
Requires: perl-module-Time-modules
Requires: perl-module-CGI.pm

%description
Log::Dispatch is a suite of OO modules for logging messages to
multiple outputs, each of which can have a minimum and maximum log
level.  It is designed to be easily subclassed, both for creating a
new dispatcher object and particularly for creating new outputs.

It also allows both global (dispatcher level) and local (logging
object) message formatting callbacks which allows greater flexibility
and should reduce the need for subclassing.

Subclassing is only needed to send a message to a different output,
not to change the message format.

Please see the Log::Dispatch documentation for more details.

%prep

%build

%install

%files
