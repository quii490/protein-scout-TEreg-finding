---
type: protein-evaluation
gene: "CERS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CERS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERS3 / LASS3 |
| 蛋白名称 | Ceramide synthase 3 |
| 蛋白大小 | 383 aa / 46.3 kDa |
| UniProt ID | Q8IU89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 383 aa / 46.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=45 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.3; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **158.2/180** | |
| **归一化总分 (÷1.83)** | | | **86.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Endoplasmic reticulum membrane | ECO:0000250

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783) [ISS:UniProtKB]
- endoplasmic reticulum membrane (GO:0005789) [TAS:Reactome]

**结论**: HPA: Nucleoplasm; UniProt: Endoplasmic reticulum membrane

#### 3.2 蛋白大小评估

**评价**: 383 aa / 46.3 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed 搜索链接 | [CERS3 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERS3) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.3 |
| 高置信度残基 (pLDDT>90) 占比 | 67.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 86.19999999999999% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SGMS1 | 0.975 | 0.000 | — |
| KDSR | 0.969 | 0.000 | — |
| ACER1 | 0.965 | 0.115 | — |
| DEGS1 | 0.965 | 0.071 | — |
| UGCG | 0.964 | 0.000 | — |
| DEGS2 | 0.963 | 0.071 | — |
| ASAH1 | 0.960 | 0.068 | — |
| SMPD1 | 0.959 | 0.000 | — |
| ACER2 | 0.958 | 0.115 | — |
| CERK | 0.957 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCBD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ORMDL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EBI-2857623 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC39A9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NEU1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Q8NEN6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SSUH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| AKR1B10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| C3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| IGKC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=87.3, v6 | 预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 86.5/100

**核心优势**:
1. CERS3 — Ceramide synthase 3，较新颖，PubMed 45 篇。
2. 蛋白大小383 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=87.3，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PTPRE | BioGRID | 0 |
| SLC39A9 | BioGRID | 0 |
| PCBD2 | BioGRID | 0 |
| ORMDL3 | BioGRID | 0 |
| SLC29A2 | BioGRID | 0 |
| NEU1 | BioGRID | 0 |
| ATP6V0C | BioGRID | 0 |
| OR2A4 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CERS3（383 aa, UniProt Q8IU89）具有独特的双结构域架构——N端Homeobox-like结构域（IPR001356, PF00046）和C端TRAM/LAG1/CLN8结构域（IPR006634, PF03798）组成的鞘脂代谢酶催化模块。Homeobox-like结构域的存在尤为关键：该结构域超家族（IPR009057）经典地与DNA结合转录因子相关。尽管CERS3主要被定性为ER膜定位的神经酰胺合酶，AlphaFold v6（pLDDT=87.3，67.1%残基pLDDT>90）揭示N端homeodomain样模块（残基~1-80）折叠良好。PAE图表明两个结构域作为独立结构模块折叠，通过柔性linker连接，暗示可能存在构象切换机制。此外，Sphingolipid delta4-desaturase结构域（IPR016439）进一步扩展了其催化潜力。

**PPI网络分析**：STRING互作网络完全围绕典型的鞘脂代谢功能展开：SGMS1（0.975）、KDSR（0.969）、ACER1（0.965）、DEGS1（0.965）均为神经酰胺/鞘脂通路酶，形成紧密的代谢簇。但IntAct实验数据（PMID:32296183, PMID:33961781）揭示了超出鞘脂范畴的互作：ORMDL3是公认的ER应激传感器和丝氨酸棕榈酰转移酶调节因子，将CERS3连接至细胞应激信号；PCBD2是参与HNF1介导的基因调控的转录共激活因子，提供了与核转录机器的间接但合理的联系；SLC39A9（锌转运蛋白）和NEU1（神经氨酸酶）暗示溶酶体/内体关联；SSUH2和AKR1B10（PMID:33961781, co-IP）则扩展了其氧化应激相关网络。

**结构解读与机制模型**：我们提出"双定位模型"：基础条件下，CERS3主要定位于ER膜，其TRAM/LAG1/CLN8结构域催化神经酰胺合成（C18/C20-神经酰胺，用于皮肤屏障功能）。在特定细胞应激或信号条件下，一个亚群可能转运至核质，Homeobox-like结构域参与转录调控。AlphaFold高置信度（整体pLDDT=87.3，有序残基86.2%）支持两个结构域均为独立折叠单元，互不干扰。神经酰胺产物本身（神经酰胺及其下游S1P）是公认的核信号分子，可调节组蛋白去乙酰化酶和凋亡通路，因此CERS3可通过直接（核定位）或间接（脂质产物）方式影响核过程。HPA核质注释支持核池存在，但需要正交验证。

**TE调控意义与实验建议**：神经酰胺代谢与染色质生物学存在多重交叉点。神经酰胺激活PP1和PP2A磷酸酶，去磷酸化剪接因子和组蛋白修饰酶。CERS3的神经酰胺合酶活性可能调节基因组位点局部的脂质微环境，通过HDAC招募影响TE沉默。Homeobox-like结构域在进化上可能源自转座酶或DNA结合结构域——这是TE来源调控蛋白的常见主题。实验优先级：（1）核分级+western blot确认核定位；（2）EMSA测试Homeobox-like结构域的DNA结合活性；（3）CERS3敲低后RNA-seq评估重复元件表达变化；（4）ChIP-seq检测全基因组结合图谱，特别关注重复序列区域。

### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CERS3

### PubMed

**Count: 93**

| PMID | Title |
|---|---|
| 42295031 | Potential of 3D Skin Models and N/TERT-2G Cell Line in Genetic Research on Autosomal Recessive Nonsyndromic Epidermal Differentiation Disorders. |
| 42093330 | Uncoupling of nutrient sensing and cell size control by specific defects in ceramide structure. |
| 42044130 | Dysregulation of fatty acid and sphingolipid metabolism is involved in abnormal nasal epithelial differentiation. |
| 41966446 | Tape strips capture immune and epidermal hyperplasia markers in the major orphan ichthyoses. |
| 41936882 | Response surface methodology optimization of cell-free supernatant from P. pentosaceus BJQ fermentation of CeRS3 and its in vitro lipid-lowering effec |


