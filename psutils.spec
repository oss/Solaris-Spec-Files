%include perl-header.spec

Name: psutils
Version: 17
Release: 3
Summary: PostScript Utilities
License: BSD-like
Group: Applications/Printing
Source: psutils.tar.gz
BuildRoot: /var/tmp/%{name}-root
BuildRequires: perl

%description
Psutils is a set of scripts and programs that manipulate PostScript documents:

PROGRAMS

psbook          rearranges pages into signatures
psselect        selects pages and page ranges
pstops          performs general page rearrangement and selection
psnup           put multiple pages per physical sheet of paper
psresize        alter document paper size
epsffit         fits an EPSF file to a given bounding box

psselect in modeled after Chris Torek's dviselect program, and pstops is
modeled after Tom Rokicki's dvidvi program. psbook is modeled on my own
dvibook program, which borrows heavily from Chris Torek's dviselect.

SCRIPTS

getafm   (sh)   outputs PostScript to retrieve AFM file from printer
showchar (sh)   outputs PostScript to draw a character with metric info
fixdlsrps (perl) filter to fix DviLaser/PS output so that PSUtils works
fixfmps  (perl) filter to fix framemaker documents so that psselect etc. work
fixmacps (perl) filter to fix Macintosh documents with saner version of md
fixpsditps (perl) filter to fix Transcript psdit documents to work with PSUtils
fixpspps (perl) filter to fix PSPrint PostScript so that psselect etc. work
fixscribeps (perl) filter to fix Scribe PostScript so that psselect etc. work
fixtpps  (perl) filter to fix Troff Tpscript documents
fixwfwps (perl) filter to fix Word for Windows documents for PSUtils
fixwpps  (perl) filter to fix WordPerfect documents for PSUtils
fixwwps  (perl) filter to fix Windows Write documents for PSUtils
extractres (perl) filter to extract resources from PostScript files
includeres (perl) filter to include resources into PostScript files
psmerge (perl) hack script to merge multiple PostScript files

        [taken from the README file]

%prep
%setup -q -n psutils

%build
make -f Makefile.unix PERL=%{perl_binary}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
for i in psbook psselect pstops epsffit psnup psresize; do
        echo Installing $i;
        install -c -m 0755 $i $RPM_BUILD_ROOT/usr/local/bin;
done
for i in fixfmps fixmacps fixpsditps fixpspps fixtpps fixwfwps fixwpps fixscribeps fixwwps fixdlsrps extractres includeres psmerge getafm showchar; do
        echo Installing $i;
        install -c -m 0755 $i $RPM_BUILD_ROOT/usr/local/bin;
done
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
for i in psbook.1 psselect.1 pstops.1 epsffit.1 psnup.1 psresize.1 psmerge.1 fixscribeps.1 getafm.1 fixdlsrps.1 fixfmps.1 fixmacps.1 fixpsditps.1 fixpspps.1 fixtpps.1 fixwfwps.1 fixwpps.1 fixwwps.1 extractres.1 includeres.1; do
        echo Installing manual page for $i;
        install -c -m 0644 $i $RPM_BUILD_ROOT/usr/local/man/man1/$i;
done
mkdir -p $RPM_BUILD_ROOT/usr/local/share/psutils
for i in md68_0.ps md71_0.ps; do
        echo Installing $i;
        install -c -m 0644 $i $RPM_BUILD_ROOT/usr/local/share/psutils;
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
/usr/local/bin/*
/usr/local/man/man1/*
/usr/local/share/psutils/*
