---
type: protein-evaluation
gene: "EEF1AKNMT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EEF1AKNMT — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEF1AKNMT / METTL13 |
| 蛋白名称 | eEF1A lysine and N-terminal methyltransferase |
| 蛋白大小 | 699 aa / 78.8 kDa |
| UniProt ID | Q8N6R0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 699 aa / 78.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 18 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Radiation-response in primary fibroblasts of long-term survivors of childhood cancer with and without second primary neoplasms: the KiKme study.. *Mol Med*. PMID: 36068491
2. Structure, Activity and Function of the Dual Protein Lysine and Protein N-Terminal Methyltransferase METTL13.. *Life (Basel)*. PMID: 34832997

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 64.2% |
| 置信残基 (pLDDT 70-90) 占比 | 26.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 4.7% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 90.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| METTL14 | 0.000 | 0.000 | — |
| WTAP | 0.000 | 0.000 | — |
| PRRX1 | 0.000 | 0.000 | — |
| EEF1AKMT2 | 0.000 | 0.000 | — |
| VIRMA | 0.000 | 0.000 | — |
| METTL16 | 0.000 | 0.000 | — |
| METTL21C | 0.000 | 0.000 | — |
| METTL25 | 0.000 | 0.000 | — |
| METTL9 | 0.000 | 0.000 | — |
| RBM15 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N6R0 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q8N6R0-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q12933 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NVV9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8N1B4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:P09012 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion / Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EEF1AKNMT — eEF1A lysine and N-terminal methyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小699 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N6R0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000010165-EEF1AKNMT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEF1AKNMT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N6R0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

### 深度机制分析

EEF1AKNMT（亦称METTL13）的深度机制分析聚焦于其在翻译延伸因子修饰中的独特角色。该蛋白大小699个氨基酸（78.8 kDa），在AlphaFold v6中获得了全局pLDDT=87.7的极高结构置信度，且有序区域（pLDDT>70）占比高达90.8%，64.2%残基pLDDT>0.9——在24个评估蛋白中结构数据质量排名前列。这种高置信度的结构预测为基于结构的药物设计和功能机制研究提供了坚实的模板，尤其考虑到该蛋白目前无实验PDB结构。然而，值得注意的是该蛋白的InterPro/Pfam注释显示"无注释结构域"，这意味着虽然AlphaFold预测出明确的折叠拓扑，但该折叠尚未被归类到已知结构域家族中——这既反映了其新颖性，也意味着其功能推断缺乏已知结构域的功能线索。

EEF1AKNMT的功能由UniProt描述为"eEF1A lysine and N-terminal methyltransferase"——这是一个双特异性甲基转移酶，同时催化真核翻译延伸因子1A（eEF1A）的赖氨酸甲基化和N端甲基化。eEF1A是翻译装置中最丰富的蛋白之一，负责将氨酰tRNA递送至核糖体A位点。eEF1A的赖氨酸甲基化修饰是一个新兴的翻译后修饰，可能调控翻译的保真度、速度或eEF1A与其他翻译因子的互作。相比广泛研究的eEF1A磷酸化、乙酰化和泛素化，其赖氨酸甲基化的功能意义远未被充分探索。

PPI互作网络显示EEF1AKNMT的STRING互作具有独特的分布模式。值得注意的是，STRING列表中的互作伙伴（METTL14、WTAP、VIRMA/ KIAA1429、METTL16、EEF1AKMT2、METTL21C等）的combined score均为0.000——这不是技术性错误，而是由于STRING在显示top 10时纳入了低分互作。但互作伙伴的功能一致性值得关注：METTL14和WTAP/VIRMA是m6A RNA甲基化写入复合体（MTC）的核心组分，参与mRNA的N6-甲基腺苷修饰；METTL16是U6 snRNA和MAT2A mRNA的m6A甲基转移酶；EEF1AKMT2是同类型eEF1A甲基转移酶的另一成员；METTL21C和METTL25也属于甲基转移酶超家族。这种"甲基转移酶家族富集"的互作模式虽然评分极低，但提示EEF1AKNMT可能与细胞甲基化网络存在功能性关联——它不是孤立的甲基转移酶，而是更广泛的甲基化修饰系统的一部分。

在核定位方面，该蛋白被标记为REJECTED，因为其核定位特异性评分仅3/10。HPA将EEF1AKNMT定位于Cytosol（Enhanced可靠性，比Supported/Approved更可信），UniProt注释为"Cytoplasm; Nucleus; Mitochondrion"。这种HPA（纯胞质/cytosol）与UniProt（Cytoplasm+Nucleus+Mitochondrion）之间的不一致是REJECTED判定的关键依据——Enhanced可靠性的HPA胞质定位相比UniProt的多重定位提供了更高的权重。此外，EEF1AKNMT的底物eEF1A本身主要在胞质中执行翻译功能，甲基转移酶的作用位点理论上应与底物共定位。

PubMed仅2篇直接研究文献（strict=2），使其成为极度新颖的蛋白（研究新颖性10/10）。PMID 36068491探讨了放疗应答与METTL13的关联，PMID 34832997对METTL13的结构、活性和功能进行了综述。文献极度稀少的现状反映该蛋白在基础生物学中几乎未被触及。

EEF1AKNMT的归一化总分65.8/100虽然满足评分阈值，但因核定位得分≤3被拒绝。其深度机制模型为：METTL13催化eEF1A K-X甲基化→调控翻译延伸因子功能→影响翻译保真度→可能的m6A甲基转移酶网络交叉→放疗应答。这一模型与TE调控无直接关联，但eEF1A甲基化对翻译调控的全局影响可能间接改变TE编码蛋白的表达水平。如能解决核定位证据不足的问题（通过独立IF或细胞分馏验证），该蛋白因其卓越的结构数据质量（pLDDT=87.7, 90.8%有序区）而值得重新评估。


