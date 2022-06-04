<template>
  <div class="home">
    <h1 class="title">Vueango</h1>
    <hr>
    <div class="columns">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Add Task</h2>
          <div class="field">
            <label class="label">Description</label>
            <div class="control">
              <input class="input" type="text"  v-model="description">
            </div>
          </div>

          <div class="field">
            <label class="label">Status</label>
            <div class="control">
              <div class="select">
                <select  v-model="status">
                  <option value="todo">To do</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-6">
        <h2 class="subtitle">To do</h2>
        <div class="todo" v-for="task in tasks" v-bind:key="task.id">
          <div class="card"  v-if="task.status === 'todo'">
            <div class="card-content">{{task.description}}</div>
            <footer class="card-footer">
              <a class="card-footer-item" @click="setStatus(task.id, 'done')">Done</a>
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Done</h2>
        <div class="done"  v-for="task in tasks" v-bind:key="task.id">
          <div class="card"  v-if="task.status === 'done'">
            <div class="card-content" >{{task.description}}</div>
             <footer class="card-footer">
              <a class="card-footer-item" @click="setStatus(task.id, 'todo')">To do</a>
              <a class="card-footer-item" @click="deleteNote(task.id)">Delete</a>
            </footer>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

const API_URL = 'http://ec2-3-91-56-73.compute-1.amazonaws.com/'
import axios from 'axios'
export default {
  name: 'HomeView',
  data() {
    return {
      tasks: [],
      description: '',
      status: 'todo'
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks(){
      axios({
        method: 'get',
        url: API_URL + 'api/tasks/'
      }).then(response => this.tasks = response.data)
    },
     addTask() {
      if (this.description) {
        axios({
          method: 'post',
          url: API_URL + 'api/tasks/',
          data: {
            description: this.description,
            status: this.status
          },
        }).then((response) => {
          let newTask = {
            'id': response.data.id,
            'description': this.description,
            'status': this.status
          }
          this.tasks.push(newTask)
          this.description = ''
          this.status = 'todo'
        }).catch((error) => {
          console.log(error)
        })
      }
    },
     setStatus(task_id, status) {
      const task = this.tasks.filter(task => task.id === task_id)[0]
      const description = task.description
      axios({
        method: 'put',
        url: API_URL + 'api/tasks/' + task_id + '/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: {
          status: status,
          description: description
        },
      }).then(() => {
        task.status = status
      })
    },
     deleteNote(task_id) {
      // const task = this.tasks.filter(task => task.id === task_id)[0]
      axios({
        method: 'delete',
        url: API_URL + 'api/tasks/' + task_id + '/',
      }).then(this.getTasks())
    }
  }
}
</script>

<style lang="scss">
.select,
select {
  width: 100%;
}

.card {
  margin-bottom: 20px;
}

.done {
  opacity: 0.3;
}
</style>
