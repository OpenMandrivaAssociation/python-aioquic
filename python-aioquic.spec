%define module aioquic

Name:		python-aioquic
Version:	1.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/aioquic/%{module}-%{version}.tar.gz
Summary:	An implementation of QUIC and HTTP/3
URL:		https://pypi.org/project/aioquic/
License:	BSD-3-Clause
Group:		Development/Python
BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	python%{pyver}dist(certifi)
BuildRequires:	python%{pyver}dist(cryptography)
BuildRequires:	python%{pyver}dist(pylsqpack)
BuildRequires:	python%{pyver}dist(pyopenssl)
BuildRequires:	python%{pyver}dist(service-identity)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)


%description
aioquic is a library for the QUIC network protocol in Python.

It features a minimal TLS 1.3 implementation, a QUIC stack and an HTTP/3 stack.

aioquic is used by Python opensource projects such as dnspython, hypercorn,
mitmproxy and the Web Platform Tests cross-browser test suite.

It has also been used extensively in research papers about QUIC.

%prep
%autosetup -n %{module}-%{version} -p1

%build
export CFLAGS="%{optflags}"
%py_build

%install
%py_install
rm %{buildroot}%{python3_sitearch}/%{module}/*.c

%files
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}.dist-info
%license LICENSE
