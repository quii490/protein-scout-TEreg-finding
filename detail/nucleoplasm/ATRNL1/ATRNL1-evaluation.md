---
type: protein-evaluation
gene: "ATRNL1"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATRNL1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | ATRNL1 / Attractin-like protein 1 |
| 蛋白大小 | 1379 aa / 152.6 kDa |
| UniProt ID | Q5VV63 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA IF Approved: Nucleoplasm + Mitochondria (dual); A-431/U-251MG 双定位 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1379 aa (1200-2000 aa区间) |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 26篇 (21-50区间) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT 80.50 (mean), 81.0% >70, 无PDB |
| 调控结构域 | 7/10 | ×2 | 14 | EGF/CUB/Kelch/C-lectin/PSI domains, baseline |
| PPI 网络 | 4/10 | ×3 | 12 | IntAct 125条, 多元互作, 部分调控相关 |
| 互证加分 | — | max +3 | +0.5 | Protein Atlas Approved + AlphaFold 高质量互相印证 |
| **原始总分** |  |  | **123.5/183** |  |
| **归一化总分** |  |  | **67.5/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm (approved) + Mitochondria (approved) | Approved |
| UniProt | Membrane | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ATRNL1/IF_images/A431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ATRNL1/IF_images/U251MG_1.jpg|U-251MG]]

**结论**: 核质+线粒体双定位。HPA Approved。2/3 细胞系显示核质+线粒体共定位 (A-431, U-251MG)，U2OS 仅显示线粒体。UniProt 标注为 Membrane 蛋白，但 HPA IF 未显示膜定位。核质定位为实验确认 (Approved)。

#### 3.2 蛋白大小评估
**评价**: 1379 aa, 152.6 kDa。较大的蛋白 (1200-2000 aa 区间)，生化操作有一定挑战性。但结构域排列清晰（多个独立折叠域），可分段研究。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 26 |
| 最早发表年份 | 2009 |
| Chromatin/epigenetics 比例 | 极低 |

**主要研究方向**:
- 腹主动脉瘤 (ceRNA 网络预测)
- MGRN1 E3 ubiquitin ligase 互作 (transmembrane adaptor)
- 绵羊长寿性状 GWAS
- RET fusion 泛癌分析
- 细胞迁移与增殖

**关键文献**:
1. Du J et al. (2026). "A predictive insight into the ATRNL1-mediated ceRNA network driving abdominal aortic aneurysm progression via VSMC phenotypic switching". *Biochem Biophys Res Commun*. PMID: 42061003
2. Parashara P et al. (2025). "The E3 ubiquitin ligase MGRN1 targets melanocortin receptors MC1R and MC4R via interactions with transmembrane adapters". *J Cell Sci*. PMID: 41178558
3. Pinto LFB et al. (2025). "Genome-wide association and functional annotation analyses reveal candidate genes and pathways associated with various ewe longevity indicators in U.S. Katahdin sheep". *Front Genet*. PMID: 40678382
4. Parashara P et al. (2025). "The E3 ubiquitin ligase MGRN1 targets melanocortin receptors MC1R and MC4R via interactions with transmembrane adapters". *bioRxiv*. PMID: 40196599
5. Zhao Y et al. (2025). "The fusion characteristics of RET fusion in pan-cancer among the Chinese population: A comprehensive genomic analysis". *Transl Oncol*. PMID: 40184718

**评价**: 26 篇，属于 21-50 区间，新颖性评分 8。研究多为关联分析或泛癌筛选，无直接功能研究。ATRNL1 作为核质蛋白的功能角色完全未探索。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 80.50 |
| pLDDT >90 占比 | 40.4% |
| pLDDT 70-90 占比 | 40.6% |
| pLDDT <50 占比 | 10.3% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ATRNL1/ATRNL1-PAE.png]]

**评价**: AlphaFold 高质量预测 (mean pLDDT 80.50)，81.0% 残基 pLDDT >70。多个独立折叠域（CUB, EGF, Kelch propeller, PSI, C-lectin, Laminin EGF）在 AlphaFold 中均有高置信度折叠。仅 N 端 (1-23) 和 C 端 (1354-1379) 末端无序。多结构域排列清晰，可对单个域进行结构研究。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt InterPro | C-type lectin, CUB, EGF, Kelch-type beta-propeller, PSI, Laminin EGF, Attractin-like CTLD |
| Pfam | Beta-prop_ATRN-LZTR1, CUB, EGF_LMN_ATRN, EGF_Teneurin, GBD_ATRN, PSI |
| SMART | CLECT, CUB, EGF, EGF_Lam, PSI |

**染色质调控潜力分析**: 所有结构域均为胞外/膜蛋白典型结构域。CUB + EGF + PSI + C-lectin 排列提示分泌/膜蛋白功能（类似 Attractin 家族）。无已知 chromatin/DNA-binding 结构域。但核质定位的生物学意义未知，可能存在未被注释的核功能。baseline 评分 (7)。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | 功能类别 | 调控相关？ |
|---|---|---|---|
| 多跨膜/信号蛋白 | Two-hybrid/co-IP | 信号转导 | 部分 |
| E3 ubiquitin ligase 途径蛋白 | co-IP | 泛素化 | 是 |

**STRING 预测互作**: API 不可用，基于 IntAct 推断。

**已知复合体成员** (GO Cellular Component):
- Membrane

**PPI 互证分析**:
- IntAct 实验验证: 125 条记录
- GO-CC: 仅 Membrane 注释
- 调控相关比例: 部分 partner 涉及泛素化途径和信号转导

**评价**: IntAct 数据丰富 (125 条)，多数互作反映其膜/分泌蛋白特性。MGRN1 E3 泛素连接酶互作 (Parashara et al. 2025) 是近期实验验证。核质定位的 PPI 数据缺失，反映核功能尚未被研究。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | Protein Atlas IF / UniProt | Nucleoplasm vs Membrane | 不一致 |
| 结构域 | UniProt / InterPro / Pfam / SMART | 多胞外结构域 多库确认 | 一致 |

**互证加分明细**:
- 结构域多库一致: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: (2/5)

**核心优势**:
1. 核质定位 Approved (HPA IF)
2. AlphaFold 高质量 (80.50 mean pLDDT)，多独立折叠域
3. IntAct 数据丰富

**风险/不确定性**:
1. 结构域全部为胞外/膜类型，与核定位矛盾
2. UniProt 标注 Membrane，与 HPA 核定位不一致
3. 核功能完全未知，缺乏研究基础
4. 蛋白大 (1379 aa)，研究核功能需要证明非膜定位

**下一步建议**:
- [ ] 独立验证核定位 (排除膜蛋白污染)
- [ ] 确认是否存在核定位信号 (NLS)

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VV63
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107518-ATRNL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22ATRNL1%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VV63


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[ATRNL1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ATRNL1/ATRNL1-PAE.png]]




