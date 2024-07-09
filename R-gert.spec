#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v3
# autospec commit: c1050fe
#
Name     : R-gert
Version  : 2.0.1
Release  : 58
URL      : https://cran.r-project.org/src/contrib/gert_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gert_2.0.1.tar.gz
Summary  : Simple Git Client for R
Group    : Development/Tools
License  : MIT
Requires: R-gert-lib = %{version}-%{release}
Requires: R-askpass
Requires: R-credentials
Requires: R-openssl
Requires: R-rstudioapi
Requires: R-sys
Requires: R-zip
BuildRequires : R-askpass
BuildRequires : R-credentials
BuildRequires : R-openssl
BuildRequires : R-rstudioapi
BuildRequires : R-sys
BuildRequires : R-zip
BuildRequires : buildreq-R
BuildRequires : libgit2-dev
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
support for SSH and HTTPS remotes. All functions in 'gert' use basic R data 
    types (such as vectors and data-frames) for their arguments and return values.
    User credentials are shared with command line 'git' through the git-credential
    store and ssh keys stored on disk or ssh-agent.

%package lib
Summary: lib components for the R-gert package.
Group: Libraries

%description lib
lib components for the R-gert package.


%prep
%setup -q -n gert
pushd ..
cp -a gert buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701829104

%install
export SOURCE_DATE_EPOCH=1701829104
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gert/DESCRIPTION
/usr/lib64/R/library/gert/INDEX
/usr/lib64/R/library/gert/LICENSE
/usr/lib64/R/library/gert/Meta/Rd.rds
/usr/lib64/R/library/gert/Meta/features.rds
/usr/lib64/R/library/gert/Meta/hsearch.rds
/usr/lib64/R/library/gert/Meta/links.rds
/usr/lib64/R/library/gert/Meta/nsInfo.rds
/usr/lib64/R/library/gert/Meta/package.rds
/usr/lib64/R/library/gert/Meta/vignette.rds
/usr/lib64/R/library/gert/NAMESPACE
/usr/lib64/R/library/gert/NEWS
/usr/lib64/R/library/gert/R/gert
/usr/lib64/R/library/gert/R/gert.rdb
/usr/lib64/R/library/gert/R/gert.rdx
/usr/lib64/R/library/gert/WORDLIST
/usr/lib64/R/library/gert/doc/gert.R
/usr/lib64/R/library/gert/doc/gert.Rmd
/usr/lib64/R/library/gert/doc/gert.html
/usr/lib64/R/library/gert/doc/index.html
/usr/lib64/R/library/gert/help/AnIndex
/usr/lib64/R/library/gert/help/aliases.rds
/usr/lib64/R/library/gert/help/figures/logo.png
/usr/lib64/R/library/gert/help/gert.rdb
/usr/lib64/R/library/gert/help/gert.rdx
/usr/lib64/R/library/gert/help/paths.rds
/usr/lib64/R/library/gert/html/00Index.html
/usr/lib64/R/library/gert/html/R.css
/usr/lib64/R/library/gert/tests/libgit2.R
/usr/lib64/R/library/gert/tests/libgit2.Rout.save
/usr/lib64/R/library/gert/tests/spelling.R
/usr/lib64/R/library/gert/tests/testthat.R
/usr/lib64/R/library/gert/tests/testthat/ecdsa.key
/usr/lib64/R/library/gert/tests/testthat/ed25519.key
/usr/lib64/R/library/gert/tests/testthat/key.pem
/usr/lib64/R/library/gert/tests/testthat/pat.bin
/usr/lib64/R/library/gert/tests/testthat/rsa3072.key
/usr/lib64/R/library/gert/tests/testthat/test-auth.R
/usr/lib64/R/library/gert/tests/testthat/test-clone.R
/usr/lib64/R/library/gert/tests/testthat/test-commit.R
/usr/lib64/R/library/gert/tests/testthat/test-config.R
/usr/lib64/R/library/gert/tests/testthat/test-ignore.R
/usr/lib64/R/library/gert/tests/testthat/test-merge.R
/usr/lib64/R/library/gert/tests/testthat/test-open.R
/usr/lib64/R/library/gert/tests/testthat/test-rebase.R
/usr/lib64/R/library/gert/tests/testthat/test-remotes.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gert/libs/gert.so
/usr/lib64/R/library/gert/libs/gert.so.avx2
/usr/lib64/R/library/gert/libs/gert.so.avx512
