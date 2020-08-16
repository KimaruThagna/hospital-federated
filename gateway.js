const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require("@apollo/gateway");

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'doctors', url: 'http://localhost:1337' },
    { name: 'diagnosis', url: 'http://localhost:1339' },
    { name: 'patients', url: 'http://localhost:1338' },
  ],
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});