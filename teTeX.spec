%include machine-header.spec

Name: teTeX
Version: 1.0.7
Release: 2
Copyright: GPL
Group: Applications/Text
Source: teTeX-src-1.0.7.tar.gz
BuildRoot: /var/tmp/%{name}-root
Summary: Thomas Esser's TeX distribution

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
%setup -q -n teTeX-1.0
mkdir -p $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf
gzip -dc $RPM_SOURCE_DIR/teTeX-texmf-1.0.2.tar.gz \
  | (umask 0 ; cd $RPM_BUILD_ROOT/usr/local/teTeX/share/texmf ; tar xvf -)

%build
./configure --prefix=$RPM_BUILD_ROOT/usr/local/teTeX
make world

%install
# nothing

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
