#Newer versions of perl-module-MIME-tools need File::Temp 
#that's incompatible with Solaris 9's perl 5.6.1. We're 
#stopping builds of this package at 5.420 until we no longer use Solaris 9.


%include perl-header.spec

Summary: 	MIME-tools
Name: 		perl-module-MIME-tools
Version: 	5.423
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	MIME-tools-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl
BuildRequires: 	perl

Requires: perl-module-IO-stringy

Provides: perl-module-MIME-Body
Provides: perl-module-MIME-Decoder
Provides: perl-module-MIME-Decoder-Base64
Provides: perl-module-MIME-Decoder-Binary
Provides: perl-module-MIME-Decoder-Gzip64
Provides: perl-module-MIME-Decoder-NBit
Provides: perl-module-MIME-Decoder-QuotedPrint
Provides: perl-module-MIME-Decoder-UU
Provides: perl-module-MIME-Entity
Provides: perl-module-MIME-Field-ContDisp
Provides: perl-module-MIME-Field-ContTraEnc
Provides: perl-module-MIME-Field-ContType
Provides: perl-module-MIME-Field-ParamVal
Provides: perl-module-MIME-Head
Provides: perl-module-MIME-Parser
Provides: perl-module-MIME-Parser-Filer
Provides: perl-module-MIME-Reader
Provides: perl-module-MIME-Parser-Results
Provides: perl-module-MIME-Tools
Provides: perl-module-MIME-WordDecoder
Provides: perl-module-MIME-Words

%description
MIME-tools - modules for parsing (and creating!) MIME entities

SYNOPSIS
    Here's some pretty basic code for parsing a MIME message, and outputting
    its decoded components to a given directory:

        use MIME::Parser;

        ### Create parser, and set some parsing options:
        my $parser = new MIME::Parser;
        $parser->output_under("$ENV{HOME}/mimemail");

        ### Parse input:
        $entity = $parser->parse(\*STDIN) or die "parse failed\n";

        ### Take a look at the top-level entity (and any parts it has):
        $entity->dump_skeleton;

    Here's some code which composes and sends a MIME message containing
    three parts: a text file, an attached GIF, and some more text:

        use MIME::Entity;

        ### Create the top-level, and set up the mail headers:
        $top = MIME::Entity->build(Type    =>"multipart/mixed",
                                   From    => "me\@myhost.com",
                                   To      => "you\@yourhost.com",
                                   Subject => "Hello, nurse!");

        ### Part #1: a simple text document:
        $top->attach(Path=>"./testin/short.txt");

        ### Part #2: a GIF file:
        $top->attach(Path        => "./docs/mime-sm.gif",
                     Type        => "image/gif",
                     Encoding    => "base64");

        ### Part #3: some literal text:
        $top->attach(Data=>$message);

        ### Send it:
        open MAIL, "| /usr/lib/sendmail -t -oi -oem" or die "open: $!";
        $top->print(\*MAIL);
        close MAIL;

    For more examples, look at the scripts in the examples directory of the
    MIME-tools distribution.

DESCRIPTION
    MIME-tools is a collection of Perl5 MIME:: modules for parsing,
    decoding, *and generating* single- or multipart (even nested multipart)
    MIME messages. (Yes, kids, that means you can send messages with
    attached GIF files).

REQUIREMENTS
    You will need the following installed on your system:

            File::Path
            File::Spec
            IPC::Open2              (optional)
            IO::Scalar, ...         from the IO-stringy distribution
            MIME::Base64
            MIME::QuotedPrint
            Net::SMTP
            Mail::Internet, ...     from the MailTools distribution.

    See the Makefile.PL in your distribution for the most-comprehensive list
    of prerequisite modules and their version numbers.


%prep

%setup -q -n MIME-tools-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

perl Makefile.PL
gmake


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
gmake test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README
# Note: we can just do %{site_perl}/MIME/* but that wouldn't allow for new
# MIMe-Decoder-* modules, for example
# Well -- actually if such module exists it will probably get added to this package
# so we can do it either way. For now I'll leave this like this ;)
%{site_perl}/MIME/Body.pm
%{site_perl}/MIME/Decoder.pm
%{site_perl}/MIME/Decoder/Base64.pm
%{site_perl}/MIME/Decoder/Binary.pm
%{site_perl}/MIME/Decoder/Gzip64.pm
%{site_perl}/MIME/Decoder/NBit.pm
%{site_perl}/MIME/Decoder/QuotedPrint.pm
%{site_perl}/MIME/Decoder/UU.pm
%{site_perl}/MIME/Decoder/BinHex.pm
%{site_perl}/MIME/Entity.pm
%{site_perl}/MIME/Field/ConTraEnc.pm
%{site_perl}/MIME/Field/ContDisp.pm
%{site_perl}/MIME/Field/ContType.pm
%{site_perl}/MIME/Field/ParamVal.pm
%{site_perl}/MIME/Head.pm
%{site_perl}/MIME/Parser.pm
%{site_perl}/MIME/Parser/Filer.pm
%{site_perl}/MIME/Parser/Reader.pm
%{site_perl}/MIME/Parser/Results.pm
%{site_perl}/MIME/Tools.pm
%{site_perl}/MIME/WordDecoder.pm
%{site_perl}/MIME/Words.pm
%{site_perl_arch}/auto/MIME-tools
%{perl_prefix}/man/man3/*

%changelog
* Wed Nov 7 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 5.423-1
- Updated to latest version (5.423).


