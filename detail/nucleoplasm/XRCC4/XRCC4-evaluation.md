---
type: protein-evaluation
gene: "XRCC4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## XRCC4 — REJECTED (研究热度过高 (PubMed strict=568，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XRCC4 |
| 蛋白名称 | DNA repair protein XRCC4 |
| 蛋白大小 | 336 aa / 38.3 kDa |
| UniProt ID | Q13426 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 336 aa / 38.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=568 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.8; PDB: 1FU1, 1IK9, 3II6, 3MUD, 3Q4F, 3RWR, 3SR2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010585, IPR014751, IPR038051, IPR053963, IPR053 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- DNA ligase IV complex (GO:0032807)
- DNA-dependent protein kinase-DNA ligase 4 complex (GO:0005958)
- nonhomologous end joining complex (GO:0070419)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 568 |
| PubMed broad count | 905 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Dynamic assemblies and coordinated reactions of non-homologous end joining.. *Nature*. PMID: 40500445
2. Structural analysis of the basal state of the Artemis:DNA-PKcs complex.. *Nucleic acids research*. PMID: 35801871
3. PAXX binding to the NHEJ machinery explains functional redundancy with XLF.. *Science advances*. PMID: 37256950
4. Ligase IV syndrome.. *European journal of medical genetics*. PMID: 19467349
5. ATP-dependent DNA ligases.. *Genome biology*. PMID: 11983065

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 56.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 31.8% |
| 有序区域 (pLDDT>70) 占比 | 60.8% |
| 可用 PDB 条目 | 1FU1, 1IK9, 3II6, 3MUD, 3Q4F, 3RWR, 3SR2, 3W03, 4XA4, 5CHX |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1FU1, 1IK9, 3II6, 3MUD, 3Q4F, 3RWR, 3SR2, 3W03, 4XA4, 5CHX）+ AlphaFold极高置信度预测（pLDDT=74.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010585, IPR014751, IPR038051, IPR053963, IPR053962; Pfam: PF06632, PF21925, PF21924 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NHEJ1 | 0.999 | 0.988 | — |
| PRKDC | 0.999 | 0.976 | — |
| APLF | 0.999 | 0.741 | — |
| XRCC5 | 0.999 | 0.897 | — |
| XRCC6 | 0.999 | 0.940 | — |
| LIG4 | 0.999 | 0.997 | — |
| PAXX | 0.999 | 0.292 | — |
| APTX | 0.998 | 0.742 | — |
| IFFO1 | 0.994 | 0.975 | — |
| PNKP | 0.993 | 0.783 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000421491.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| rnk | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PAXX | psi-mi:"MI:0096"(pull down) | pubmed:21712045|imex:IM-17900 |
| IQCF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VASH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPM1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XRCC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CD81 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-24070|pubmed:26212323 |
| GAGE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EMX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 1FU1, 1IK9, 3II6, 3MUD, 3Q4F,  | pLDDT=74.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. XRCC4 — DNA repair protein XRCC4，研究基础较多，新颖性有限。
2. 蛋白大小336 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 568 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 568 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13426
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152422-XRCC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XRCC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13426
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
