from PySide import QtCore, QtGui


class SeriesModel(QtCore.QAbstractListModel):
	def __init__(self, series, conn, parent=None):
		QtCore.QAbstractListModel.__init__(self, parent)
		self._series = series
		self.conn = conn

	def rowCount(self,role):
		return len(self._series)

	def setDatas(self, series):
		self._series = series
		start = self.createIndex(0,0)
		end = self.createIndex(len(self._series)-1, 0)
		self.dataChanged.emit(start, end)

	def setData(self, index, value, role=QtCore.Qt.EditRole):
		if role != QtCore.Qt.EditRole:
			return False
		if index.isValid() and 0 <= index.row() < len(self._series):
			self._series[index.row()] = value
			self.dataChanged.emit(index, index)

	def indexFor(self, obj):
		return self.index(self._series.index(obj),0)

	def data(self, index, role):
		if role == QtCore.Qt.DisplayRole:
			return "(%s) %s" % (self._series[index.row()].start,self._series[index.row()].title)
		elif role == QtCore.Qt.FontRole:
			if self._series[index.row()].fav:
				return QtGui.QFont('Sans Serif', 10, QtGui.QFont.Bold)
			return None
		elif role == QtCore.Qt.DecorationRole:
			img = self.conn.getFirstCover(self._series[index.row()])
			if img:
				qimg = QtGui.QImage.fromData(img, 'JPG')
			else:
				img = open('res/missing.png', 'rb').read()
				qimg = QtGui.QImage.fromData(img, 'png')
			qpix = QtGui.QPixmap.fromImage(qimg)
			return QtGui.QIcon(qpix)
		elif role == QtCore.Qt.UserRole:
			return self._series[index.row()]
		else:
			return None

class IssueModel(QtCore.QAbstractListModel):
	def __init__(self, conn, parent=None):
		QtCore.QAbstractListModel.__init__(self, parent)
		self.conn = conn
		self._issues = []

	def append(self, issue):
		self.beginInsertRows(QtCore.QModelIndex(), len(self._issues)-1,
				len(self._issues))
		self._issues.append(issue)
		index = self.index(len(self._issues)-1, 0)
		self.endInsertRows()
		self.dataChanged.emit(index, index)

	def setChanged(self, index):
		if index.isValid() and 0 <= index.row() < len(self._issues):
			self.dataChanged.emit(index, index)

	def setData(self, index, value, role=QtCore.Qt.UserRole):
		if role != QtCore.Qt.UserRole:
			return False
		if index.isValid() and 0 <= index.row() < len(self._issues):
			self._issues[index.row()] = value
			self.dataChanged.emit(index, index)

	def indexFor(self, obj):
		if obj in self._issues:
			return self.index(self._issues.index(obj),0)
		else:
			return None

	def rowCount(self, role):
		return len(self._issues)

	def data(self, index, role):
		issue = self._issues[index.row()]
		if role == QtCore.Qt.DisplayRole:
			return "#%s" % (issue.safe_nr)
		elif role == QtCore.Qt.DecorationRole:
			if issue.hasCover():
				qimg = QtGui.QImage.fromData(issue.cover(), 'JPG')
			else:
				img = open('res/missing.png', 'rb').read()
				qimg = QtGui.QImage.fromData(img, 'png')
			if self.conn.issueHasLocal(issue):
				okpix = QtGui.QPixmap('res/ok.png')
			elif issue.downloading or self.conn.issueHasTemp(issue):
				okpix = QtGui.QPixmap('res/tango/go-bottom.png')
			else:
				okpix = QtGui.QPixmap('res/notok.png')
			qpix = QtGui.QPixmap.fromImage(qimg)
			qrect = qpix.rect()
			miniokpix = okpix.scaled(64,64)
			painter = QtGui.QPainter(qpix)
			painter.drawPixmap(qrect.width()-64,qrect.height()-64,miniokpix)
			painter.end()
			return QtGui.QIcon(qpix)
		elif role == QtCore.Qt.UserRole:
			return issue
		else:
			return None

class SeriesSearchResultModel(QtCore.QAbstractItemModel):
	def __init__(self, series, conn, parent=None):
		QtCore.QAbstractItemModel.__init__(self, parent)
		self._series = series
		self.conn = conn
		
	def rowCount(self, role):
		return len(self._series)

	def columnCount(self, role):
		return 3

	def headerData(self, sec, orient, role):
		print("I have been called %s" % sec)
		return(str(sec))

	def data(self, index, role):
		if not index.isValid():
			return None
		if role == QtCore.Qt.DisplayRole:
			return "Foobar"
		else:
			return None
