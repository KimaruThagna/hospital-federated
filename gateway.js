const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require("@apollo/gateway");

const gateway = new ApolloGateway({
  serviceList: [
    { name: 'doctors', url: 'http://localhost:5001' },
    { name: 'diagnosis', url: 'http://localhost:5002' },
    { name: 'patients', url: 'http://localhost:5003' },
  ],
});

const server = new ApolloServer({
  gateway,
  subscriptions: false,
});

server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});