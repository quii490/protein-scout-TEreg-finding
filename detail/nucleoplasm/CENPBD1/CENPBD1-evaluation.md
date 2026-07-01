---
type: protein-evaluation
gene: "CENPBD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CENPBD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPBD1 / CENPBD1P |
| 蛋白名称 | Putative CENPB DNA-binding domain-containing protein 1 |
| 蛋白大小 | 187 aa / 21.1 kDa |
| UniProt ID | B2RD01 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 5/10 | ×4 | 20 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 187 aa / 21.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.8; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 17 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无数据 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, revealing recurrent domestication events in vertebrates.. *Mob DNA*. PMID: 32742312
2. A prognostic mRNA expression signature of four 16q24.3 genes in radio(chemo)therapy-treated head and neck squamous cell carcinoma (HNSCC).. *Mol Oncol*. PMID: 30259648

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.8 |
| 高置信度残基 (pLDDT>90) 占比 | 12.3% |
| 置信残基 (pLDDT 70-90) 占比 | 27.3% |
| 中等置信 (pLDDT 50-70) 占比 | 35.3% |
| 低置信 (pLDDT<50) 占比 | 25.1% |
| 有序区域 (pLDDT>70) 占比 | 39.6% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPBD1/CENPBD1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=63.8），有序残基占 39.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TIGD6 | 0.000 | 0.000 | — |
| TIGD7 | 0.000 | 0.000 | — |
| SMLR1 | 0.000 | 0.000 | — |
| HUS1B | 0.000 | 0.000 | — |
| HARBI1 | 0.000 | 0.000 | — |
| NAIF1 | 0.000 | 0.000 | — |
| TIGD5 | 0.000 | 0.000 | — |
| TMEM244 | 0.000 | 0.000 | — |
| SPATA33 | 0.000 | 0.000 | — |
| JRK | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 17，IntAct interactions: 0
- 调控相关比例: 0 / 17 = 0%

**评价**: STRING 17 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.8 + PDB: 无 | pLDDT=63.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 17 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CENPBD1 — Putative CENPB DNA-binding domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小187 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KIAA1429 | BioGRID | 0 |
| DDX58 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CENPBD1（187 aa, UniProt B2RD01）具有双DNA结合结构域架构，包括N端HTH psq型结构域（IPR007889, PF03221, UniProt FT: DOMAIN 13-64, PROSITE:PRU00320）和C端HTH CENPB型结构域（IPR006600, PF04218, UniProt FT: DOMAIN 78-155, PROSITE:PRU00583），两者均属于homeodomain-like超家族（IPR009057）和winged helix-like DNA结合域超家族（IPR036388）。此串联HTH排列直接同源于着丝粒蛋白B（CENPB）的DNA结合域——CENPB识别着丝粒α-卫星DNA中的CENP-B box。然而，AlphaFold v6预测质量较差（pLDDT=63.8，仅12.3%残基>90，有序区39.6%），表明显著的结构无序。低pLDDT可能反映域间linker区域的真实柔性，以及一个或两个HTH结构域在无DNA环境下的熔球态行为——DNA结合结构域常在靶标识别时展现折叠，暗示CENPBD1可能在DNA结合时发生实质性的induced-fit构象变化。

**PPI网络与进化信号**：PPI画像极其稀疏：STRING列出17个伙伴（TIGD6、TIGD7、HARBI1、SMLR1、HUS1B、NAIF1等），但所有combined score=0.000——表明仅为text-mining或基因组邻近关联，无实验或共表达证据。IntAct互作=0，HPA interaction页面亦无数据。然而，伙伴列表本身具有深刻的进化含义：TIGD6和TIGD7是tigger DNA转座酶来源蛋白，含有CENPB型结构域；HARBI1是Harbinger转座酶来源核酸酶；JRK和POGK均属pogo超家族转座酶衍生物。CENPBD1的STRING邻域由其他驯化转座酶来源蛋白填充——这是有意义的进化信号，即使无物理互作存在。

**结构解读与机制模型**：CENPBD1最合理的模型为：通过串联HTH结构域识别类似CENP-B box的特定DNA基序的序列特异性DNA结合蛋白。CENPB本身以纳摩尔亲和力结合17bp CENP-B box（TTCGTTGGAAACGGGA），CENPBD1可能识别相关但可能分化的序列。进化来源清晰：CENPBD1源自pogo/Tc1-mariner转座酶超家族（PMID:32742312），其中串联HTH-psq + HTH-CENPB排列起源于类pogo转座子的DNA结合域。此驯化事件将转座酶转化为宿主DNA结合蛋白——哺乳动物基因组中的重复主题（如RAG1/RAG2源自Transib转座子，CENPB本身源自pogo转座酶）。低pLDDT（63.8）反常地支持DNA诱导折叠模型：HTH结构域仅在靶标DNA结合时才结构化——本质无序DNA结合域的经典特征，通过大熵罚实现高特异性。

**TE调控意义与实验建议**：CENPBD1可能是本评价集中TE调控最有吸引力的候选蛋白。一个被驯化的转座酶，带有双HTH结构域并保留在细胞核中，正是预期中参与TE识别和沉默的蛋白类型。CENPB先例极具启示性：CENPB结合着丝粒重复序列，但也识别嵌入LTR反转录转座子（如HERV-K）中的CENP-B box基序，促进其转录抑制。CENPBD1可能对不同TE亚家族执行类似监控功能。与TIGD6、TIGD7和HARBI1（全为转座酶来源蛋白）的关联（即使是text-mining）暗示参与驯化转座酶网络。极度新颖性（PubMed=2篇）意味着CENPBD1在TE生物学中的角色完全未被探索。实验优先级：（1）SELEX或ChIP-seq确定DNA结合特异性；（2）测试CENPBD1是否抑制携带CENP-B box样基序的报告基因；（3）CENPBD1过表达/敲低后TE家族特异性表达变化评估；（4）cryo-EM/X-ray解析CENPBD1与其同源DNA复合结构，确认induced-fit模型并揭示特异性决定因素。

### TE 调控评估

该蛋白具有染色质/DNA 调控相关结构域，可能参与 TE 沉默。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B2RD01
- Protein Atlas: https://www.proteinatlas.org/search/CENPBD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPBD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2RD01
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CENPBD1/CENPBD1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | B2RD01 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 13..64; /note="HTH psq-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00320"; DOMAIN 78..155; /note="HTH CENPB-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00583" |
| InterPro | IPR009057;IPR006600;IPR007889;IPR036388; |
| Pfam | PF04218;PF03221; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
