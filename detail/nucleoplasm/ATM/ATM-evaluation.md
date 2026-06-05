---
type: protein-evaluation
gene: "ATM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATM — REJECTED (研究热度过高 (PubMed strict=8756，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATM |
| 蛋白名称 | Serine-protein kinase ATM |
| 蛋白大小 | 3056 aa / 350.7 kDa |
| UniProt ID | Q13315 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Golgi apparatus; UniProt: Nucleus; Cytoplasmic vesicle; Cytoplasm, cytoskeleton, micro |
| 蛋白大小 | 0/10 | ×1 | 0 | 3056 aa / 350.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=8756 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 5NP0, 5NP1, 6HKA, 6K9K, 6K9L, 7NI4, 7NI5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR038980, IPR003152, IPR011009, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus; Cytoplasmic vesicle; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Pe... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- DNA repair complex (GO:1990391)
- extrinsic component of synaptic vesicle membrane (GO:0098850)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8756 |
| PubMed broad count | 33284 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Characterization of ATM gene mutations in 66 ataxia telangiectasia families.. *Human molecular genetics*. PMID: 9887333
2. Breast cancer risks associated with missense variants in breast cancer susceptibility genes.. *Genome medicine*. PMID: 35585550
3. Modeling ATM mutant proteins from missense changes confirms retained kinase activity.. *Human mutation*. PMID: 19431188
4. Rare, evolutionarily unlikely missense substitutions in ATM confer increased risk of breast cancer.. *American journal of human genetics*. PMID: 19781682
5. Ataxia-telangiectasia: future prospects.. *The application of clinical genetics*. PMID: 25258552

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 5NP0, 5NP1, 6HKA, 6K9K, 6K9L, 7NI4, 7NI5, 7NI6, 7SIC, 7SID |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR038980, IPR003152, IPR011009, IPR000403; Pfam: PF02259, PF02260, PF00454 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRCA1 | 0.999 | 0.847 | — |
| CHEK2 | 0.999 | 0.836 | — |
| MDC1 | 0.999 | 0.876 | — |
| MSH6 | 0.999 | 0.324 | — |
| TP53 | 0.999 | 0.928 | — |
| MRE11 | 0.999 | 0.907 | — |
| MSH2 | 0.999 | 0.324 | — |
| NBN | 0.999 | 0.989 | — |
| ATR | 0.999 | 0.974 | — |
| TP53BP1 | 0.999 | 0.874 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 5NP0, 5NP1, 6HKA, 6K9K, 6K9L,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasmic vesicle; Cytoplasm, cytoskele / Nucleoplasm, Vesicles; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATM — Serine-protein kinase ATM，研究基础较多，新颖性有限。
2. 蛋白大小3056 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 8756 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 8756 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13315
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149311-ATM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13315
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000149311-ATM/subcellular

![](https://images.proteinatlas.org/67142/2253_G10_108_blue_red_green.jpg)
![](https://images.proteinatlas.org/67142/2253_G10_189_blue_red_green.jpg)
![](https://images.proteinatlas.org/67142/1270_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/67142/1270_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/67142/1842_A5_61_red_green.jpg)
![](https://images.proteinatlas.org/67142/1842_A5_64_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
