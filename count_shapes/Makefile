PY_IMPLS := count_shapes_golf.py count_shapes_recurse.py count_shapes_sets.py
CXX_IMPLS := count_shapes_set.exe count_shapes_lambda.exe

test: test.py $(PY_IMPLS) $(CXX_IMPLS)
	python test.py

CXXFLAGS := --std=c++14

count_shapes_set.exe: main.o count_shapes_set.o
	$(CXX) $(CXXFLAGS) $^ -o $@

count_shapes_lambda.exe: main.o count_shapes_lambda.o
	$(CXX) $(CXXFLAGS) $^ -o $@
