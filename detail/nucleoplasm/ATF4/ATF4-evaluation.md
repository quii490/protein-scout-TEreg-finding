---
type: protein-evaluation
gene: "ATF4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATF4 — REJECTED (研究热度过高 (PubMed strict=3822，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATF4 / CREB2, TXREB |
| 蛋白名称 | Cyclic AMP-dependent transcription factor ATF-4 |
| 蛋白大小 | 351 aa / 38.6 kDa |
| UniProt ID | P18848 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus speckle; Cytoplasm; Cell membrane; Cytoplas |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 38.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3822 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 1CI6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm; Cell membrane; Cytoplasm, cytoskeleton, microtubule organizing ... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ATF1-ATF4 transcription factor complex (GO:1990590)
- ATF4-CREB1 transcription factor complex (GO:1990589)
- centrosome (GO:0005813)
- CHOP-ATF4 complex (GO:1990617)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite membrane (GO:0032590)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3822 |
| PubMed broad count | 5437 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CREB2, TXREB |

**关键文献**:
1. ATF4 in cellular stress, ferroptosis, and cancer.. *Archives of toxicology*. PMID: 38383612
2. eIF3d controls the persistent integrated stress response.. *Molecular cell*. PMID: 37683648
3. ER-stress-induced transcriptional regulation increases protein synthesis leading to cell death.. *Nature cell biology*. PMID: 23624402
4. Thbs1 induces lethal cardiac atrophy through PERK-ATF4 regulated autophagy.. *Nature communications*. PMID: 34168130
5. Alleviation of liver fibrosis by inhibiting a non-canonical ATF4-regulated enhancer program in hepatic stellate cells.. *Nature communications*. PMID: 39789010

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 18.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 38.7% |
| 低置信 (pLDDT<50) 占比 | 34.5% |
| 有序区域 (pLDDT>70) 占比 | 26.8% |
| 可用 PDB 条目 | 1CI6 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 26.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEBPB | 0.997 | 0.926 | — |
| DDIT3 | 0.996 | 0.526 | — |
| EIF2AK3 | 0.992 | 0.000 | — |
| ATF3 | 0.989 | 0.622 | — |
| EIF2S1 | 0.989 | 0.000 | — |
| EP300 | 0.988 | 0.791 | — |
| CREBBP | 0.987 | 0.783 | — |
| TRIB3 | 0.983 | 0.778 | — |
| PPP1R15A | 0.979 | 0.000 | — |
| CEBPG | 0.977 | 0.821 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| nuf | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG9331 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG5050 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| rb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG16719 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Nin | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Blos2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| crc | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:unassigned1513|imex:IM- |
| PTCD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HAUS7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 1CI6 | pLDDT=62.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm; Cell membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ATF4 — Cyclic AMP-dependent transcription factor ATF-4，研究基础较多，新颖性有限。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3822 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3822 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P18848
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128272-ATF4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATF4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P18848
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
