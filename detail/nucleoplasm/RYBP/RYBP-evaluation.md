---
type: protein-evaluation
gene: "RYBP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RYBP — REJECTED (研究热度过高 (PubMed strict=127，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RYBP / DEDAF, YEAF1 |
| 蛋白名称 | RING1 and YY1-binding protein |
| 蛋白大小 | 228 aa / 24.8 kDa |
| UniProt ID | Q8N488 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 24.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=127 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.6; PDB: 3IXS, 8PP6, 9DBY, 9DDE, 9DG3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039958, IPR033774, IPR001876, IPR036443; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PcG protein complex (GO:0031519)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 127 |
| PubMed broad count | 171 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DEDAF, YEAF1 |

**关键文献**:
1. Polycomb protein RYBP facilitates super-enhancer activity.. *Molecular medicine (Cambridge, Mass.)*. PMID: 39604829
2. Glucose-induced RYBP suppresses tumor cell aerobic glycolysis and migration.. *Biochemical and biophysical research communications*. PMID: 38735205
3. Epigenetic and non-epigenetic functions of the RYBP protein in development and disease.. *Mechanisms of ageing and development*. PMID: 29665352
4. De novo variants in RYBP are associated with a severe neurodevelopmental disorder and congenital anomalies.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 39891528
5. RYBP promotes HIV-1 latency through promoting H2AK119ub and decreasing H3K4me3.. *Cell communication and signaling : CCS*. PMID: 40361117

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.6 |
| 高置信度残基 (pLDDT>90) 占比 | 24.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 58.8% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 28.5% |
| 可用 PDB 条目 | 3IXS, 8PP6, 9DBY, 9DDE, 9DG3 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.6），有序残基占 28.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039958, IPR033774, IPR001876, IPR036443; Pfam: PF17219, PF00641 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KDM2B | 0.999 | 0.852 | — |
| PCGF1 | 0.999 | 0.866 | — |
| RNF2 | 0.999 | 0.990 | — |
| RING1 | 0.999 | 0.940 | — |
| YY1 | 0.998 | 0.532 | — |
| PCGF5 | 0.996 | 0.881 | — |
| BMI1 | 0.996 | 0.840 | — |
| PCGF6 | 0.996 | 0.846 | — |
| YAF2 | 0.992 | 0.781 | — |
| PCGF2 | 0.991 | 0.795 | — |

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
| 三维结构 | AlphaFold pLDDT=66.6 + PDB: 3IXS, 8PP6, 9DBY, 9DDE, 9DG3 | pLDDT=66.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus, nucleoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RYBP — RING1 and YY1-binding protein，研究基础较多，新颖性有限。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 127 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 127 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N488
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163602-RYBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RYBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N488
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
