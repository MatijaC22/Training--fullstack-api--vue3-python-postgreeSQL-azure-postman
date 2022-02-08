/*rutiranje- polje svih stranica*/
const routes=[
    {path:'/home',component:home},
    {path:'/department',component:department},
    {path:'/employee',component:employee}
]

/*novi objekt od vueroutera i dodavanje gornjeg polja*/
const router=new VueRouter({
    // mode: 'history',
    routes
})

/*kreiranje vue objekta i biti ce mounted to the element with id app*/
const app = new Vue({
    router
}).$mount('#app') /*isti id kji korisitimo u id naseg div objekta u htmlu*/


