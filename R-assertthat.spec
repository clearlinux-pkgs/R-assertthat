#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-assertthat
Version  : 0.2.0
Release  : 15
URL      : https://cran.r-project.org/src/contrib/assertthat_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/assertthat_0.2.0.tar.gz
Summary  : Easy Pre and Post Assertions
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : clr-R-helpers

%description
easy to declare the pre and post conditions that you code should
    satisfy, while also producing friendly error messages so that your
    users know what they've done wrong.

%prep
%setup -q -c -n assertthat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502400638

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502400638
export LANG=C
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
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library assertthat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library assertthat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library assertthat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
