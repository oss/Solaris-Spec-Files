%define emacs_ver 20.7
%define site_lisp /usr/local/emacs20/share/emacs/site-lisp
%define info_dir  /usr/local/emacs20/info

Summary: TeX/LaTeX mode for Emacs
Name: auctex
Version: 9.9p
Release: 2
Group: Applications/Editors
Copyright: GPL
Source: auctex.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: emacs >= %{emacs_ver}
BuildRequires: emacs >= %{emacs_ver}

%description
   AUC TeX is a comprehensive customizable integrated environment for
writing input files for LaTeX using GNU Emacs.

   AUC TeX lets you run TeX/LaTeX and other LaTeX-related tools, such
as a output filters or post processor from inside Emacs.  Especially
`running LaTeX' is interesting, as AUC TeX lets you browse through the
errors TeX reported, while it moves the cursor directly to the reported
error, and displays some documentation for that particular error.  This
will even work when the document is spread over several files.

   AUC TeX automatically indents your `LaTeX-source', not only as you
write it -- you can also let it indent and format an entire document.
It has a special outline feature, which can greatly help you `getting an
overview' of a document.

   Apart from these special features, AUC TeX provides a large range of
handy Emacs macros, which in several different ways can help you write
your LaTeX documents fast and painlessly.

  [ from README ]

%prep
%setup -q

%build
make
for i in font-latex bib-cite tex-jp ; do
    emacs -batch -q -l lpath.el -f batch-byte-compile $i.el
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{site_lisp}
mkdir -p $RPM_BUILD_ROOT%{info_dir}
make install lispdir=$RPM_BUILD_ROOT%{site_lisp}
make install-info infodir=$RPM_BUILD_ROOT%{info_dir}
for i in font-latex bib-cite tex-jp ; do
    install -m 0644 $i.elc $RPM_BUILD_ROOT%{site_lisp}
done
TEX_SITE=$RPM_BUILD_ROOT%{site_lisp}/tex-site.el
mv $TEX_SITE $TEX_SITE.OLD
sed "s#$RPM_BUILD_ROOT##" < $TEX_SITE.OLD > $TEX_SITE
rm $TEX_SITE.OLD

%post
/usr/local/bin/install-info --info-dir=%{info_dir} %{info_dir}/auctex \
  --entry="* Auctex: (auctex).                        TeX mode for Emacs"
cat <<EOF

To use auctex, you need to put (require 'tex-site) in your .emacs file.

EOF

%preun
/usr/local/bin/install-info --delete --info-dir=%{info_dir} %{info_dir}/auctex

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING CHANGES PROBLEMS README
%{site_lisp}/tex-site.el
%{site_lisp}/*.elc
%{site_lisp}/auctex
%{info_dir}/auctex*
