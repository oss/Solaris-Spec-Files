%include perl-header.spec

Summary: MIME-tools
Name: perl-module-MIME-tools
Version: 5.411a
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: MIME-tools-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

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

%setup -q -n MIME-tools-5.411

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl_arch}/*
%{site_perl}/*
%{perl_prefix}/man/man3/*
