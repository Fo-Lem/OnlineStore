<script lang="ts">
import AdminInput from '../UI/adminInput.vue'
import { login } from './http/login'

export default {
  name: 'AdminAuth',
  components: {
    AdminInput,
  },
  data() {
    return {
      login: 'secrAd56',
      password: 'gveih5yh.5',
    }
  },
  methods: {
    async authAdmin() {
      await login(this.login, this.password)
      if (localStorage.getItem('token'))
        console.log(localStorage.getItem('token'))
      this.$router.push('/_adminPanel')
    },
  },
}
</script>

<template>
  <div class="flex flex-col items-center justify-center ">
    <div class="w-96">
      <h3 class="text-lg text-center">
        Авторизация
      </h3>
      <form @submit.prevent="authAdmin">
        <AdminInput
          input-name="Логин"
          input-in="login"
          :value="login"
          @update-input="(value) => login = value"
        />
        <AdminInput
          input-name="Пароль"
          input-in="password"
          :value="password"
          @update-input="(value) => password = value"
        />
        <button
          type="submit"
          class="mt-5 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
        >
          Войти
        </button>
      </form>
    </div>
  </div>
</template>
./http/auth
./http/login
