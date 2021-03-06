from sqlalchemy.orm import Query as _Query





class Query(_Query):
    def first_or_404(self):
        """Like :meth:`first` but raise NotFound()  instead of returning ``None``."""

        rv = self.first()
        if rv is None:
            raise BaseException()
        return rv