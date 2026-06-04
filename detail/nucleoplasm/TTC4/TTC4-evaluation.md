---
type: protein-evaluation
gene: "TTC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC4 |
| 蛋白名称 | Hsp70/Hsp90 co-chaperone CNS1 homolog |
| 蛋白大小 | 387 aa / 44.7 kDa |
| UniProt ID | O95801 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Intermediate filaments; 额外: Cytoplasmic bodies; UniProt: Nucleus; Nucleus, nucleoplasm; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 387 aa / 44.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.9; PDB: 6HFO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR044059, IPR011990, IPR019734; Pfam: PF18972 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Intermediate filaments; 额外: Cytoplasmic bodies | Enhanced |
| UniProt | Nucleus; Nucleus, nucleoplasm; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A naturally occurring SNP modulates thermotolerance divergence among grapevines.. *Nature communications*. PMID: 40450013
2. 1 Cellular protein TTC4 and its cofactor HSP90 are pro-viral for bovine herpesvirus 1.. *Virus research*. PMID: 36100007
3. Promoting TTC4 and HSP70 interaction and translocation of annexin A7 to lysosome inhibits apoptosis in vascular endothelial cells.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 33000523
4. TTC4 inhibits NLRP3 inflammation in rheumatoid arthritis by HSP70.. *International journal of rheumatic diseases*. PMID: 37431792
5. The human TPR protein TTC4 is a putative Hsp90 co-chaperone which interacts with CDC6 and shows alterations in transformed cells.. *PloS one*. PMID: 18320024

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.9 |
| 高置信度残基 (pLDDT>90) 占比 | 63.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 86.1% |
| 可用 PDB 条目 | 6HFO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.9，有序区 86.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044059, IPR011990, IPR019734; Pfam: PF18972 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HGH1 | 0.991 | 0.988 | — |
| HSP90AB1 | 0.897 | 0.756 | — |
| HSP90AA1 | 0.887 | 0.731 | — |
| RPS7 | 0.795 | 0.000 | — |
| PPID | 0.783 | 0.321 | — |
| SMAD3 | 0.774 | 0.045 | — |
| CDC37 | 0.756 | 0.239 | — |
| VPS29 | 0.745 | 0.734 | — |
| VPS35 | 0.729 | 0.727 | — |
| VPS26A | 0.699 | 0.688 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TCOF1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 21362046 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000360329.3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| HSP90AA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19875381 |
| TUBA1A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SERPINB13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.9 + PDB: 6HFO | pLDDT=86.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Cytoplasm / Intermediate filaments; 额外: Cytoplasmic bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TTC4 — Hsp70/Hsp90 co-chaperone CNS1 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小387 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95801
- Protein Atlas: https://www.proteinatlas.org/ENSG00000243725-TTC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95801
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
