
test: test.py count_shapes_golf.py count_shapes_recurse.py count_shapes_sets.py count_shapes_exe.py count_shapes_set count_shapes_lambda
	python test.py

CXXFLAGS := --std=c++14

count_shapes_set: main.o count_shapes_set.o
	$(CXX) $(CXXFLAGS) $^ -o $@

count_shapes_lambda: main.o count_shapes_lambda.o
	$(CXX) $(CXXFLAGS) $^ -o $@
