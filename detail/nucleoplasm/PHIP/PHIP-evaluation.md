---
type: protein-evaluation
gene: "PHIP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PHIP — REJECTED (研究热度过高 (PubMed strict=445，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHIP / DCAF14, WDR11 |
| 蛋白名称 | PH-interacting protein |
| 蛋白大小 | 1821 aa / 206.7 kDa |
| UniProt ID | Q8WWQ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli rim; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1821 aa / 206.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=445 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 3MB3, 5ENB, 5ENC, 5ENE, 5ENF, 5ENH, 5ENI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052060, IPR001487, IPR036427, IPR018359, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli rim | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 445 |
| PubMed broad count | 1955 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DCAF14, WDR11 |

**关键文献**:
1. De novo genic mutations among a Chinese autism spectrum disorder cohort.. *Nature communications*. PMID: 27824329
2. PhIP-Seq characterization of serum antibodies using oligonucleotide-encoded peptidomes.. *Nature protocols*. PMID: 30190553
3. PHIP-associated Chung-Jansen syndrome: Report of 23 new individuals.. *Frontiers in cell and developmental biology*. PMID: 36726590
4. PHIP gene variants with protein modeling, interactions, and clinical phenotypes.. *American journal of medical genetics. Part A*. PMID: 34773373
5. Phage display sequencing reveals that genetic, environmental, and intrinsic factors influence variation of human antibody epitope repertoire.. *Immunity*. PMID: 37164013

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 31.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 35.1% |
| 有序区域 (pLDDT>70) 占比 | 57.6% |
| 可用 PDB 条目 | 3MB3, 5ENB, 5ENC, 5ENE, 5ENF, 5ENH, 5ENI, 5ENJ, 5RJI, 5RJJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 57.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052060, IPR001487, IPR036427, IPR018359, IPR057451; Pfam: PF00439, PF25437, PF25313 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DDB1 | 0.910 | 0.857 | — |
| CUL4B | 0.898 | 0.830 | — |
| CUL4A | 0.895 | 0.846 | — |
| ATRX | 0.742 | 0.100 | — |
| BDP1 | 0.687 | 0.000 | — |
| TAF1 | 0.684 | 0.567 | — |
| RSF1 | 0.682 | 0.331 | — |
| BUB3 | 0.668 | 0.554 | — |
| NIPBL | 0.647 | 0.000 | — |
| SMG1 | 0.640 | 0.066 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TUBB4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| STMN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| tkt1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NR4A1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| CUL4B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HNRNPCL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TPR | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 3MB3, 5ENB, 5ENC, 5ENE, 5ENF,  | pLDDT=66.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PHIP — PH-interacting protein，研究基础较多，新颖性有限。
2. 蛋白大小1821 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 445 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 445 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWQ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146247-PHIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWQ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
