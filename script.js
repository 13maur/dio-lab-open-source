const url = "https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/cyclist-data.json";
const width = 800;
const height = 500;
const padding = 60;

const svg = d3.select("#chart")
              .attr("width", width)
              .attr("height", height);

d3.json(url).then(data => {
    const dataset = data;

    // Escalas
    const xScale = d3.scaleLinear()
                     .domain([d3.min(dataset, d => d.Year) - 1, d3.max(dataset, d => d.Year) + 1])
                     .range([padding, width - padding]);

    const yScale = d3.scaleTime()
                     .domain([d3.min(dataset, d => new Date(`1970-01-01T00:${d.Time}Z`)), 
                              d3.max(dataset, d => new Date(`1970-01-01T00:${d.Time}Z`))])
                     .range([height - padding, padding]);

    // Eixos
    const xAxis = d3.axisBottom(xScale).tickFormat(d3.format("d"));
    const yAxis = d3.axisLeft(yScale).tickFormat(d3.timeFormat("%M:%S"));

    svg.append("g")
       .attr("id", "x-axis")
       .attr("transform", `translate(0, ${height - padding})`)
       .call(xAxis);

    svg.append("g")
       .attr("id", "y-axis")
       .attr("transform", `translate(${padding}, 0)`)
       .call(yAxis);

    // Adicionar pontos
    svg.selectAll(".dot")
       .data(dataset)
       .enter()
       .append("circle")
       .attr("class", "dot")
       .attr("cx", d => xScale(d.Year))
       .attr("cy", d => yScale(new Date(`1970-01-01T00:${d.Time}Z`)))
       .attr("r", 5)
       .attr("data-xvalue", d => d.Year)
       .attr("data-yvalue", d => new Date(`1970-01-01T00:${d.Time}Z`));

    // Tooltip
    const tooltip = d3.select("#tooltip");

    svg.selectAll(".dot")
       .on("mouseover", (event, d) => {
           tooltip.style("display", "block")
                  .style("left", event.pageX + "px")
                  .style("top", event.pageY - 30 + "px")
                  .attr("data-year", d.Year)
                  .text(`Ano: ${d.Year}, Tempo: ${d.Time}`);
       })
       .on("mouseout", () => tooltip.style("display", "none"));
});
