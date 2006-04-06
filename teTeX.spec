%include machine-header.spec

Name: teTeX
Version: 3.0
Release: 2
Copyright: GPL
Group: Applications/Text
Source: ftp://tug.ctan.org/tex-archive/systems/unix/teTeX/current/distrib/tetex-src-3.0.tar.gz
Source1: ftp://tug.ctan.org/tex-archive/systems/unix/teTeX/current/distrib/tetex-texmf-3.0.tar.gz
Source2: teTeX-3.0.0.patch
BuildRoot: %{_tmppath}/%{name}-root
Provides: tetex
BuildRequires: patch
Summary: Thomas Esser''s TeX distribution

%description 

teTeX is a complete TeX and LaTeX system---it includes TeX, LaTeX,
metafont (with all the font paths set up and all of the fonts
included), metapost, web, and more.  TeX is a document formatting
system developed by Donald Knuth that is especially good at formatting
mathematics.  You should install this if you want to format really
good-looking texts (think Art of Computer Programming 3rd editions,
Concrete Mathematics, various mathematics and physics journals).
teTeX can also be used to format texinfo documentation.

%prep
%setup -q -n tetex-src-3.0
mkdir -p $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf
gzip -dc $RPM_SOURCE_DIR/tetex-texmf-3.0.tar.gz \
  | (umask 0 ; cd $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf ; tar xvf -)

%build
CC="/opt/SUNWspro/bin/cc"
CXX="/opt/SUNWspro/bin/CC"
LD="/usr/ccs/bin/ld"
LDFLAGS="-L/usr/local/lib -L/usr/sfw/lib -R/usr/local/lib -R/usr/sfw/lib"
CPPFLAGS="-I/usr/local/include -I/usr/sfw/include"
PATH="/usr/local/gnu/bin:/usr/local/lib:/usr/sfw/bin:/usr/local/ssl/lib:$PATH"
export CC
export CXX
export LD
export LDFLAGS
export CPPFLAGS
export PATH

#sed -e "s|$(SHELL) ${srcdir}/mkinstalldirs $(bindir) $(man1dir)|$(SHELL) ${srcdir}/mkinstalldirs $(DESTDIR)$(bindir) $(DESTDIR)$(man1dir)|" utils/dialog/Makefile.in > utils/dialog/Makefile.in2
#mv utils/dialog/Makefile.in2 utils/dialog/Makefile.in

#./configure --prefix=/usr/local/teTeX --disable-multiplatform
./configure --prefix=%{buildroot}/usr/local/teTeX --disable-multiplatform
make all

%install
#make install DESTDIR=%{buildroot}
make install
cd $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf/dvips/config
cp config.ps config.ps.virgin
/usr/local/gnu/bin/patch < $RPM_SOURCE_DIR/teTeX-3.0.0.patch

%clean
rm -rf $RPM_BUILD_ROOT

%post
for i in latex.info texinfo web2c.info dvips.info kpathsea.info ; do
    cp /usr/local/teTeX/info/$i* /usr/local/info
    chmod 644 /usr/local/info/$i*
    if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
             /usr/local/info/$i
    fi
done

cat <<EOF
You need to add /usr/local/teTeX/bin/%{sparc_arch} to your path.
You should also run texconfig.  Finally, you also may want to execute

  chmod a+rw /usr/local/teTeX/share/texmf/ls-R

so kpathsea can cache fonts that it has compiled.
EOF



%preun
for i in latex.info texinfo web2c.info dvips.info kpathsea.info ; do
    rm /usr/local/info/$i*
    if [ -x /usr/local/bin/install-info ] ; then
        /usr/local/bin/install-info --info-dir=/usr/local/info \
             --delete /usr/local/info/$i
    fi
done


%files
%defattr(-, root, root)
/usr/local/teTeX

%changelog
* Wed Mar 22 2006 Jonathan Kaczynski <jmkacz@oss.rutgers.edu> - 3.0-2
- Rebuilt against gcc-3.4.5
* Fri Sep 05 2005 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 3.0-1
- Version 3.0
