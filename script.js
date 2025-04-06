const width = 800;
const height = 400;
const padding = 50;

const svg = d3.select("#chart")
              .attr("width", width)
              .attr("height", height);

fetch("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json")
    .then(response => response.json())
    .then(data => {
        const dataset = data.data;
        const xScale = d3.scaleBand()
                         .domain(dataset.map(d => d[0]))
                         .range([padding, width - padding])
                         .padding(0.1);
        const yScale = d3.scaleLinear()
                         .domain([0, d3.max(dataset, d => d[1])])
                         .range([height - padding, padding]);

        const xAxis = d3.axisBottom(xScale).tickFormat(d => d.slice(0, 4));
        const yAxis = d3.axisLeft(yScale);

        svg.append("g")
           .attr("id", "x-axis")
           .attr("transform", `translate(0, ${height - padding})`)
           .call(xAxis);

        svg.append("g")
           .attr("id", "y-axis")
           .attr("transform", `translate(${padding}, 0)`)
           .call(yAxis);

        svg.selectAll(".bar")
           .data(dataset)
           .enter()
           .append("rect")
           .attr("class", "bar")
           .attr("x", d => xScale(d[0]))
           .attr("y", d => yScale(d[1]))
           .attr("width", xScale.bandwidth())
           .attr("height", d => height - padding - yScale(d[1]));
    });
    console.log("O script.js está carregando corretamente!");
