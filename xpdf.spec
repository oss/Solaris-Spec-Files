%define xpdf_ver 3.01
%define source_file xpdf-%{xpdf_ver}.tar.gz
%define prefix /usr/local

Name: xpdf
Version: %{xpdf_ver}
Copyright: GPL V2 
Release: 1
Summary: A light weight PDF viewer
Group: Applications/Viewers
Source: %{source_file}
Requires: freetype2 >= 2.0.5
BuildRequires: freetype2-devel >= 2.0.5 t1lib
BuildRoot: %{_tmppath}/%{name}-root
Provides: xpdf

%description
Xpdf is an open source viewer for Portable Document Format (PDF)
files.  (These are also sometimes also called 'Acrobat' files, from
the name of Adobe's PDF software.)  The Xpdf project also includes a
PDF text extractor, PDF-to-PostScript converter, and various other
utilities.

To run xpdf, simply type:
  xpdf file.pdf

To generate a PostScript file, hit the "print" button in xpdf, or run
pdftops:
  pdftops file.pdf

To generate a plain text file, run pdftotext:
  pdftotext file.pdf

There are four additional utilities (which are fully described in
their man pages):

  pdfinfo -- dumps a PDF file's Info dictionary (plus some other
             useful information)
  pdffonts -- lists the fonts used in a PDF file along with various
              information for each font
  pdftoppm -- converts a PDF file to a series of PPM/PGM/PBM-format
              bitmaps
  pdfimages -- extracts the images from a PDF file


%prep
%setup -q

%build
CC="cc"
CXX="CC"
#CFLAGS="-xs -Xa -fast -native -xstrconst -mt"
#CXXFLAGS="-xs -noex -mt"
CPPFLAGS="-I/usr/local/include/freetype2 -I/usr/local/include"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export CC CXX CPPFLAGS LD LDFLAGS
./configure --prefix=%{prefix}  --with-freetype2-library=/usr/local/lib  --with-freetype2-includes=/usr/local/include/freetype2  --with-t1-library=/usr/local/lib --with-t1-includes=/usr/local/include 

make 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} 



%clean
[ %{buildroot} != "/" ] && [ -d %{buildroot} ] && rm -rf %{buildroot}

%post

%files
%defattr(-, root, root)
%{prefix}/bin
%{prefix}/man
%{prefix}/etc/xpdfrc

