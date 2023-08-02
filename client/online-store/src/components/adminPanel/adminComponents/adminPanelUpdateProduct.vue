<script>
export default {
  name: 'AdminPanelUpdateProduct',
  props: {
    catalog: {
      type: Object,
      require: true,
    },
    Admin: {
      type: Object,
      require: true,
    },
  },
  emits: ['updateData'],
  data() {
    return {
      size: {
        height: 'Высота',
        width: 'Ширина',
        depth: 'Глубина',
      },
      curentProduct: {},
    };
  },
  beforeMount() {
    Object.assign(this.curentProduct, this.catalog.items[this.$route.params.itemId]);
    this.curentProduct.newCategory_id = this.curentProduct.category_id;
    this.curentProduct.newProduct_type_id = this.curentProduct.product_type_id;
    this.curentProduct.newHero_id = this.curentProduct.hero_id;
    this.curentProduct.newPrice = this.curentProduct.price;
    this.sizeParser(this.curentProduct.size);
    this.curentProduct.newDescription = this.curentProduct.description;
    this.curentProduct.photos = [];
    console.log(this.curentProduct);
  },

  methods: {
    sizeParser(size) {
      const arr = size.split('x');
      this.curentProduct.size = {
        height: arr[0],
        width: arr[1],
        depth: arr[2],
      };
    },

    getElementSelected(items) {
      console.log();
      console.log(items);
      const res = {};
      for (let key in items) {
        res[key] = items[key].name;
      }
      return res;
    },
    updateSelectedCategory(select) {
      this.curentProduct.newCategory_id = select;
    },
    updateSelectedType(select) {
      this.curentProduct.newProduct_type_id = select;
    },
    async UpdateProduct() {
      console.log(this.curentProduct);
      const obj = {
        id: this.curentProduct.id,
        id_1: this.curentProduct.id_1,
        name: this.curentProduct.name,
        category_id: this.curentProduct.newCategory_id,
        product_type_id: this.curentProduct.newProduct_type_id,
        hero_id: this.curentProduct.newHero_id,
        description: this.curentProduct.newDescription,
        size: `${ this.curentProduct.size.height }x${ this.curentProduct.size.width }x${ this.curentProduct.size.depth }`,
        price: this.curentProduct.newPrice,
      };
      await this.Admin.productController.update(obj);
      this.$emit('updateData');
      this.$router.push({ name: 'products', });
    },

  },
};
</script>

<template>
  <form
    class="py-5 flex flex-col gap-5"
    @submit.prevent="UpdateProduct"
  >
    <admin-input
      input-name="Название продукта"
      input-in="productName"
      placeholder="Меч длинный &laquoАлеша Попович&raquo"
      :value="curentProduct.name"
      @updateInput="(value) => curentProduct.name = value"
    />

    <admin-select
      :key="curentProduct.name"
      :options="getElementSelected(catalog.categories)"
      select-in="Category"
      select-name="Категория"
      :curent-option="{ index: curentProduct.category_id, option: catalog.categories[curentProduct.category_id].name }"
      @changeOptionCategory="(select) => updateSelectedCategory(select)"
      @openAddPopup="openAddPopup = true"
      @openDeletePopup="openDeletePopup = true"
      @openUpdatePopup="openUpdatePopup = true"
    />

    <admin-select
      :key="curentProduct.newCategory_id"
      :options="getElementSelected(catalog.categories[curentProduct.newCategory_id].product_types)"
      :curent-option="{ index: curentProduct.product_type_id, option: catalog.categories[curentProduct.category_id].product_types[curentProduct.product_type_id].name }"
      select-in="Type"
      select-name="Тип"
      @changeOptionType="(select) => updateSelectedType(select)"
    />

    <admin-select
      :key="curentProduct.hero_id"
      :options="getElementSelected(catalog.heroes)"
      select-in="Hero"
      select-name="Герой"
      :curent-option="{ index: curentProduct.hero_id, option: catalog.heroes[curentProduct.hero_id].name }"
      @changeOptionHero="(select) => curentProduct.newHero_id = select"
    />

    <div class="flex flex-col gap-2">
      <div>
        <h2 class=" text-md leading-6">
          Размеры
        </h2>
        <p class=" text-xs leading-6 text-gray-400">
          (Размеры в милиметрах)
        </p>
      </div>

      <admin-input
        v-for="(item, index) in curentProduct.size"
        :key="index"
        :input-name="size[index]"
        :input-in="index"
        placeholder="300"
        :value="item"
        @updateInput="(value) => curentProduct.size[index] = value"
      />
    </div>

    <div class="flex flex-col gap-2">
      <label
        for="message"
        class="block text-md text-gray-900"
      >Описание</label>
      <textarea
        id="message"
        v-model="curentProduct.newDescription"
        rows="4"
        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
        placeholder="Write your thoughts here..."
      />
    </div>
    <admin-input
      input-name="Цена"
      input-in="price"
      placeholder="3000"
      :value="String(curentProduct.price)"
      @updateInput="(value) => curentProduct.newPrice = value"
    />

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <router-link
        class="text-sm font-semibold leading-6 text-gray-900"
        :to="{ name: 'products' }"
      >
        Отменить
      </router-link>
      <button
        type="submit"
        class="rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
      >
        Изменить
      </button>
    </div>
  </form>
</template>
