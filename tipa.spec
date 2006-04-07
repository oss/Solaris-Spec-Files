%define tetex_dir	/usr/local/teTeX/share/texmf
%define tex_dir		%{tetex_dir}/tex/latex/tipa
%define font_dir	%{tetex_dir}/fonts
%define mapdir_dir	%{tetex_dir}/dvips/config

Name: tipa
Version: 1.3
Release: 1
Copyright: OpenSource
Group: Applications/Text
Summary: IPA/Phonetic Fonts for LaTeX (teTeX)
Source: tipa.zip
BuildRoot: /var/tmp/%{name}-root
#BuildRequires: tetex
Requires: tetex

%description
TIPA is a system for processing IPA (International Phonetic Alphabet)
symbols in LaTeX.  It's based on TSIPA but both METAFONT source code and
LaTeX macros have been thoroughly rewritten so it can be considered as a
new system.  (from tipaman.pdf)

CTAN: http://www.ctan.org/tex-archive/fonts/tipa/

%prep
%setup -q -n tipa

%build
PATH="/usr/local/teTeX/bin:/usr/local/gnu/bin:/usr/local/bin:${PATH}"
export PATH

cd tipa-%{version}/  # Yeah, there is another directory in there

mv Makefile Makefile.stage1
sed "s|^PREFIX=/usr/local/teTeX/share/texmf|PREFIX=${RPM_BUILD_ROOT}/usr/local/teTeX/share/texmf|" Makefile.stage1 > Makefile.stage2
sed "s|-mktexlsr|#-mktexlsr|" Makefile.stage2 > Makefile
rm -f Makefile.stage?

%install
rm -rf $RPM_BUILD_ROOT

PATH="/usr/local/teTeX/bin:/usr/local/gnu/bin:/usr/local/bin:${PATH}"
export PATH

cd tipa-1.3/

gmake install

%post
PATH="/usr/local/teTeX/bin:/usr/local/bin:${PATH}"
export PATH

echo Running mktexlsr
mktexlsr
echo done.

%postun
PATH="/usr/local/teTeX/bin:/usr/local/bin:${PATH}"
export PATH

echo Running mktexlsr
mktexlsr
echo done.

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
/usr/local/teTeX/*
