---
type: protein-evaluation
gene: "DTX3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DTX3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTX3 / RNF154 |
| 蛋白名称 | E3 ubiquitin-protein ligase DTX3 |
| 蛋白大小 | 347 aa / 38.0 kDa |
| UniProt ID | Q8N9I9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Golgi apparatus; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 347 aa / 38.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039396, IPR039399, IPR039398, IPR001841, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Golgi apparatus | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

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
| PubMed strict count | 26 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF154 |

**关键文献**:
1. The DTX Protein Family: An Emerging Set of E3 Ubiquitin Ligases in Cancer.. *Cells*. PMID: 37443713
2. Ubiquitylation of nucleic acids by DELTEX ubiquitin E3 ligase DTX3L.. *EMBO reports*. PMID: 39242775
3. DTX3 suppresses bladder cancer cell invasion and metastasis by inhibiting the Notch signaling pathway.. *International immunopharmacology*. PMID: 40127622
4. Ubiquitin ligase DTX3 empowers mutant p53 to promote ovarian cancer development.. *Genes & diseases*. PMID: 35782979
5. Ubiquitination of NOTCH2 by DTX3 suppresses the proliferation and migration of human esophageal carcinoma.. *Cancer science*. PMID: 31854042

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.2% |
| 置信残基 (pLDDT 70-90) 占比 | 24.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 11.0% |
| 有序区域 (pLDDT>70) 占比 | 78.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.4，有序区 78.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039396, IPR039399, IPR039398, IPR001841, IPR013083; Pfam: PF18102, PF13923 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PARP9 | 0.848 | 0.000 | — |
| NOTCH2 | 0.821 | 0.314 | — |
| NOTCH4 | 0.774 | 0.071 | — |
| NOTCH1 | 0.740 | 0.071 | — |
| NOTCH3 | 0.739 | 0.071 | — |
| ANK2 | 0.670 | 0.050 | — |
| ANK3 | 0.642 | 0.050 | — |
| ANK1 | 0.639 | 0.050 | — |
| UBE2D1 | 0.637 | 0.232 | — |
| CHFR | 0.615 | 0.601 | — |

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
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 无 | pLDDT=82.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nucleoli; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DTX3 — E3 ubiquitin-protein ligase DTX3，非常新颖，仅有少数基础研究。
2. 蛋白大小347 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9I9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178498-DTX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9I9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
