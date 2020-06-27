html = b"""
<html>
    <body>
        <form method="get" action="">
            <p>
                A: <input type="number" name="a">
            </p>
            <p>
                B: <input type="number" name="b">
            </p>
            <p>
                <input type="submit">
            </p>
        </form>
        <p>
            Sum : %(sum)s</br>
            Mul : %(mul)s</br>
        </p>
    </body>
</html>
"""
