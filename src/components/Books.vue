<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Books</h1>
        <hr />
        <button
          type="button"
          @click="BookDiolog"
          class="btn btn-success btn-sm"
        >
          Add Book
        </button>
        <br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read == 'true'">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button
                  type="button"
                  @click="UpdateDiolog(book)"
                  class="btn btn-warning btn-sm"
                >
                  Update
                </button>
                <button
                  type="button"
                  @click="DeleteDiolog(book)"
                  class="btn btn-danger btn-sm">
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <div id="AddBookForm" class="card w-75" v-show="formDisplay">
          <div class="card-body">
            <h5 class="card-title">Add Book</h5>
            <button
              type="button"
              @click="CloseDiolog"
              class="btn-close"
              aria-label="Close"
            ></button>
            <form class="row g-3">
              <div class="col-md-4">
                <label for="inputTitle" class="form-label">Title</label>
                <input
                  type="text"
                  class="form-control"
                  id="inputTitle"
                  v-model="BookForm.title"
                  placeholder="Please Fill in title"
                />
              </div>
              <div class="col-md-4">
                <label for="inputAuthor" class="form-label">Author</label>
                <input
                  type="text"
                  class="form-control"
                  id="inputAuthor"
                  v-model="BookForm.author"
                  placeholder="Please Fill in author"
                />
              </div>
              <div class="col-md-4">
                <label for="inputRead" class="form-label">Read</label>
                <select
                  id="inputRead"
                  class="form-select"
                  v-model="BookForm.read"
                >
                  <option>true</option>
                  <option>false</option>
                </select>
              </div>
            </form>
            <div class="errorMessage">
              {{ formErrorMes }}
            </div>
            <button
              type="submit"
              class="btn btn-success"
              @click="onSubmit"
              variant="primary"
            >
              Submit
            </button>
            <button
              type="reset"
              class="btn btn-primary"
              @click="onReset"
              variant="danger"
            >
              Reset
            </button>
          </div>
        </div>
        <!-- updated Form -->
        <div
          id="AddupdateForm"
          class="card w-75"
          v-show="editFormDisplay"
          ref="editBookModal"
        >
          <div class="card-body">
            <h5 class="card-title">Update Book</h5>
            <button
              type="button"
              @click="CloseDiolog"
              class="btn-close"
              aria-label="Close"
            ></button>
            <form class="row g-3">
              <div class="col-md-4">
                <label for="inputTitle" class="form-label">Title</label>
                <input
                  type="text"
                  class="form-control"
                  id="inputTitle"
                  v-model="editForm.title"
                  placeholder="Please Fill in title"
                />
              </div>
              <div class="col-md-4">
                <label for="inputAuthor" class="form-label">Author</label>
                <input
                  type="text"
                  class="form-control"
                  id="inputAuthor"
                  v-model="editForm.author"
                  placeholder="Please Fill in author"
                />
              </div>
              <div class="col-md-4">
                <label for="inputRead" class="form-label">Read</label>
                <select
                  id="inputRead"
                  class="form-select"
                  v-model="editForm.read"
                >
                  <option>true</option>
                  <option>false</option>
                </select>
              </div>
            </form>
            <div class="errorMessage">
              {{ editErrorMes }}
            </div>
            <button
              type="submit"
              class="btn btn-success"
              @click="onSubmitUpdate"
              variant="primary"
            >
              Update
            </button>
            <button
              type="reset"
              class="btn btn-primary"
              @click="CloseDiolog"
              variant="danger"
            >
              Cancel
            </button>
          </div>
        </div>

        <!-- delete Form -->
        <div
          id="AdddeleteForm"
          class="card w-75"
          v-show="deleteFormDisplay"
          ref="editBookModal"
        >
          <div class="card-body">
            <h5 class="card-title">Delete Book</h5>
            <button
              type="button"
              @click="CloseDiolog"
              class="btn-close"
              aria-label="Close"
            ></button>
            <form class="row g-3">
              <div class="col-md-4">
                <label for="inputTitle" class="form-label">Title</label>
                <input
                  type="text"
                  class="form-control"
                  id="inputTitle"
                  v-model="deleteForm.title"
                  disabled
                />
              </div>
              <div class="col-md-4">
                <label for="inputAuthor" class="form-label">Author</label>
                <input
                  type="text"
                  class="form-control"
                  id="inputAuthor"
                  v-model="deleteForm.author"
                  disabled
                />
              </div>
              <div class="col-md-4">
                <label for="inputRead" class="form-label">Read</label>
                <select
                  id="inputRead"
                  class="form-select"
                  v-model="deleteForm.read"
                  disabled
                >
                  <option>true</option>
                  <option>false</option>
                </select>
              </div>
            </form>
            <div class="errorMessage">
              {{ deleteErrorMes }}
            </div>
            <button
              type="submit"
              class="btn btn-danger"
              @click="onDeleteBook"
            >
              Delete
            </button>
            <button
              type="reset"
              class="btn btn-primary"
              @click="CloseDiolog"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
      BookForm: {
        title: '',
        author: '',
        read: '',
      },
      formDisplay: false,
      formErrorMes: '',
      editForm: {
        id: '',
        title: '',
        author: '',
        read: '',
      },
      editFormDisplay: false,
      editErrorMes: '',
      deleteForm: {
        id: '',
        title: '',
        author: '',
        read: '',
      },
      deleteFormDisplay: false,
      deleteErrorMes: '',
    };
  },
  methods: {
    getBooks() {
      const path = 'https://booklist-byfei.herokuapp.com/v1/books/';
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'https://booklist-byfei.herokuapp.com/v1/books/';
      axios
        .post(path, payload)
        .then((res) => {
          if (res.data.status === 'Failed') {
            this.formErrorMes = res.data.message;
          } else {
            this.formErrorMes = '';
            this.getBooks();
            this.initForm();
            this.formDisplay = false;
          }
          console.log(res);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    updateBook(payload) {
      const path = 'https://booklist-byfei.herokuapp.com/v1/books/';
      axios
        .put(path, payload)
        .then((res) => {
          if (res.data.status === 'Failed') {
            this.editErrorMes = res.data.message;
          } else {
            this.editErrorMes = '';
            this.getBooks();
            this.editFormDisplay = false;
          }
          console.log(res);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    removeBook(payload) {
      const path = 'https://booklist-byfei.herokuapp.com/v1/books/';
      axios
        .delete(path, payload)
        .then((res) => {
          if (res.data.status === 'Failed') {
            this.deleteErrorMes = res.data.message;
          } else {
            this.deleteErrorMes = '';
            this.getBooks();
            this.deleteFormDisplay = false;
          }
          console.log(res);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    initForm() {
      this.BookForm.title = '';
      this.BookForm.author = '';
      this.BookForm.read = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      let flg = 'false';
      console.log(this.BookForm.read);
      if (this.BookForm.read === 'true') {
        flg = 'true';
      }
      const payload = {
        title: this.BookForm.title,
        author: this.BookForm.author,
        read: flg,
      };
      this.addBook(payload);
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      const payload = {
        id: this.editForm.id,
        title: this.editForm.title,
        author: this.editForm.author,
        read: this.editForm.read,
      };
      this.updateBook(payload);
    },
    // axois put & post 接受三個參數: url, data, config
    // delete 接口只接受兩個參數: url, config
    // 故必須將資料包在data裡面再傳
    onDeleteBook(evt) {
      evt.preventDefault();
      const payload = {
        data: {
          id: this.deleteForm.id,
        },
      };
      this.removeBook(payload);
    },
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
    BookDiolog() {
      this.formDisplay = true;
    },
    UpdateDiolog(book) {
      this.editFormDisplay = true;
      this.editForm.id = book.id;
      this.editForm.title = book.title;
      this.editForm.author = book.author;
      this.editForm.read = book.read;
    },
    DeleteDiolog(book) {
      this.deleteFormDisplay = true;
      this.deleteForm.id = book.id;
      this.deleteForm.title = book.title;
      this.deleteForm.author = book.author;
      this.deleteForm.read = book.read;
    },
    CloseDiolog() {
      this.formDisplay = false;
      this.editFormDisplay = false;
      this.deleteFormDisplay = false;
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
<style scoped>
input,
select {
  margin-bottom: 15px;
}
button {
  margin: 0 0.5rem;
}
#AddBookForm,
#AddupdateForm,
#AdddeleteForm {
  position: fixed;
  top: 25vw;
  left: 13vw;
}
.errorMessage {
  margin: 1rem;
  color: #ff0000;
}
.btn-close {
  position: absolute;
  right: 1rem;
  top: 1rem;
}
</style>
