<script lang="ts">
import AdminInput from '../UI/adminInput.vue'

export default {
  name: 'AdminAuth',
  components: {
    AdminInput,
  },
  data() {
    return {
      login: '',
      password: '',
    }
  },
}
</script>

<template>
  <div>
    <h3>Авторизация</h3>
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
  </div>
</template>
