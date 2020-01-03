#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-assertthat
Version  : 0.2.1
Release  : 40
URL      : https://cran.r-project.org/src/contrib/assertthat_0.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/assertthat_0.2.1.tar.gz
Summary  : Easy Pre and Post Assertions
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# assertthat
[![Travis-CI Build Status](https://travis-ci.org/hadley/assertthat.svg?branch=master)](https://travis-ci.org/hadley/assertthat)
[![Coverage status](https://codecov.io/gh/hadley/assertthat/branch/master/graph/badge.svg)](https://codecov.io/github/hadley/assertthat?branch=master)

%prep
%setup -q -c -n assertthat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571796840

%install
export SOURCE_DATE_EPOCH=1571796840
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library assertthat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library assertthat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library assertthat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc assertthat || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/assertthat/DESCRIPTION
/usr/lib64/R/library/assertthat/INDEX
/usr/lib64/R/library/assertthat/Meta/Rd.rds
/usr/lib64/R/library/assertthat/Meta/features.rds
/usr/lib64/R/library/assertthat/Meta/hsearch.rds
/usr/lib64/R/library/assertthat/Meta/links.rds
/usr/lib64/R/library/assertthat/Meta/nsInfo.rds
/usr/lib64/R/library/assertthat/Meta/package.rds
/usr/lib64/R/library/assertthat/NAMESPACE
/usr/lib64/R/library/assertthat/R/assertthat
/usr/lib64/R/library/assertthat/R/assertthat.rdb
/usr/lib64/R/library/assertthat/R/assertthat.rdx
/usr/lib64/R/library/assertthat/help/AnIndex
/usr/lib64/R/library/assertthat/help/aliases.rds
/usr/lib64/R/library/assertthat/help/assertthat.rdb
/usr/lib64/R/library/assertthat/help/assertthat.rdx
/usr/lib64/R/library/assertthat/help/paths.rds
/usr/lib64/R/library/assertthat/html/00Index.html
/usr/lib64/R/library/assertthat/html/R.css
/usr/lib64/R/library/assertthat/tests/testthat.R
/usr/lib64/R/library/assertthat/tests/testthat/test-assert-that.R
/usr/lib64/R/library/assertthat/tests/testthat/test-assertions.R
/usr/lib64/R/library/assertthat/tests/testthat/test-base-comparison.R
/usr/lib64/R/library/assertthat/tests/testthat/test-base.R
/usr/lib64/R/library/assertthat/tests/testthat/test-file.R
/usr/lib64/R/library/assertthat/tests/testthat/test-on-failure.R
/usr/lib64/R/library/assertthat/tests/testthat/test-scalar.R
