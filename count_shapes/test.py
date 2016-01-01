import count_shapes_golf
import count_shapes_sets
import count_shapes_recurse
import count_shapes_exe

test_targets = (
    count_shapes_sets,
    count_shapes_golf,
    count_shapes_recurse,
    count_shapes_exe.CountShapesExe("./count_shapes_set.exe"),
    count_shapes_exe.CountShapesExe("./count_shapes_lambda.exe"))

tests = [
    [ 'single cell grid', 1, list('X') ],

    [ 'single point', 1, list('.X.') ],

    [ 'single row', 3, list('X.X.X') ],

    [ 'single col', 3, ['X'], ['.'], ['X'], ['.'], ['X'] ],

    [ 'corners only', 4,
      list('X.X'),
      list('...'),
      list('X.X')
    ],

    [ '"U" shape', 1,
      list('X.X'),
      list('XXX')
    ],

    [ '"n" shape', 1,
      list('XXX'),
      list('X.X')
    ],

    [ '"C" shape', 1,
      list('XXX'),
      list('X..'),
      list('XXX')
    ],

    [ 'Reversed "C" shape', 1,
      list('XXX'),
      list('X..'),
      list('XXX')
    ],

    [ '"X" shape', 1,
      list('X.X'),
      list('XXX'),
      list('X.X')
    ],

    [ '"I" shape', 1,
      list('XXX'),
      list('.X.'),
      list('XXX')
    ],

    [ 'diagonals X', 1,
      list('X.X'),
      list('.X.'),
      list('X.X')
    ],

    [ 'Original Example', 4,
      list('....................'),
      list('..X.................'),
      list('..X................X'),
      list('..X.....X.X........X'),
      list('.......XXXX..XX.....'),
      list('........X...X..X....'),
      list('............XXXX....'),
      list('....................')
    ],

    [ 'Irregular row lengths', 2,
      list('...X'),
      list('....X.X'),
      list('.X.X'),
      list('..X')
    ],
]

verbose = False
class g:
  count = 0
  fail_count = 0

def DoTest(name, expect, *image):
  for pkg in test_targets:
    g.count += 1
    actual = pkg.CountShapes(image)
    if actual != expect:
      g.fail_count += 1
      print '%s: expect %d found %d for %s' % (pkg.__name__, expect, actual, name)
    elif verbose:
      print 'OK: %s (%s)' % (name, pkg.__name__,)

for test in tests:
  DoTest(*test)

print "%d fail of %d tests" % (g.fail_count, g.count)
