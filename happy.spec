Vendor:       Z101-Solutions, Munich, Germany
Distribution: Softies
Name:         happy
Version:      1.8
Release: 2
Copyright:    BSD w/o adv. clause
Group:        Development/Languages/Haskell
Packager:     Sven.Panne@informatik.uni-muenchen.de
URL:          http://www.dcs.gla.ac.uk/fp/software/happy.html
Source:       happy-1.8-src.tar.gz 
Summary:      The LALR(1) Parser Generator for Haskell
BuildRoot:    /free/tmp/%{name}-root
BuildRequires: ghc

%description
This is the nth public release of our parser generator system for
Haskell, called Happy (a dyslexic acronym for 'A Yacc-like Haskell
Parser generator').  Happy is written in Haskell, uses a parser
generated by itself, and can be compiled using ghc, hbc or gofer.

The output parser can be compiled under *any* Haskell compiler,
as well as Mark Jones' Gofer interpreter.

Authors:
--------
    Simon Marlow <simonmar@microsoft.com>
    Andy Gill <andy@dcs.gla.ac.uk>

%prep
%setup

%build
autoheader
autoconf
./configure --prefix=/usr/local --enable-hc-boot
make ProjectsToBuild="glafp-utils happy" WithHappyHc=ghc HC=ghc boot
make ProjectsToBuild="glafp-utils happy" WithHappyHc=ghc HC=ghc all

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make ProjectsToInstall=happy install prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, bin, bin)
/usr/local/bin/happy
/usr/local/bin/happy-1.8
/usr/local/lib/happy.bin
/usr/local/lib/happy
