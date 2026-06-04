---
type: protein-evaluation
gene: "AFF1"
date: 2026-05-28
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AFF1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AFF1 / AF4, MLLT2, PBM1, proto-oncogene AF4 |
| 蛋白大小 | 1210 aa / 131.4 kDa |
| UniProt ID | P51825 |
| 评估日期 | 2026-05-28 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9 | /10 | ×3 = 27 | UniProt Nucleus; PA nucleoplasm Approved; : Approved→9 |
| 蛋白大小 | 8 | /10 | ×2 = 16 | 1210 aa, 131.4 kDa |
| 研究新颖性 | 8 | /10 | ×3 = 24 | PubMed 134篇; 50-200范围; MLL融合伙伴但独立功能空间大 |
| 三维结构 | 3 | /10 | ×3 = 9 | PubMed≥100; pLDDT均值52.35, 68.6%无序→:差/大量无序→3; 1个NMR片段(2LM0, aa738-779) |
| 调控结构域 | 7 | /10 | ×2 = 14 | AF4/FMR2 CHD domain; 直接参与转录延伸调控 |
| PPI | Nucleoplasm + Mitochondria (SiHa, U2OS); HeLa 无染色 | Approved |
| GeneCards | Domain:AF4/FMR2 C-terminal homology(953-1075); Region:Disordered(80-321); Region:Disordered(373-961) |
| UniProt | Nucleus | Experimental evidence | GO | Super elongation complex, transcription elongation factor complex | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/AFF1/IF_images/SiHa_HPA069947.jpg|SiHa_HPA069947]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/AFF1/IF_images/U2OS_HPA069947.jpg|U2OS_HPA069947]]

**结论**: AFF1 是明确的核蛋白。UniProt 仅注释 Nucleus 定位。Protein Atlas IF 显示主要在核质，同时有部分线粒体信号 (SiHa, U2OS)，HeLa 细胞中无染色。作为超级延伸复合体 (SEC) 的核心组分，核定位是其主要功能场所。Protein Atlas 可靠性评定为 Approved，: Approved→评分9。

**IF 图像**:

#### 3.2 蛋白大小评估
**评价**: 1210 aa 处于 800-1200 的边界，略大于理想区间但仍在可接受范围。蛋白大部分区域 (residues 1-957) 为固有无序区 (IDR)，仅 C 端约 200 aa 具有高置信度折叠结构。IDR 可能在介导 SEC 组装中发挥 scaffold 功能，这是固有无序蛋白的典型特征。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 (narrow) | 134 |
| PubMed 总数 (broad TIAB) | 215 |
| PubMed 总数 (all) | 355 |
| 主要聚焦领域 | 白血病 (MLL-AFF1 融合), SEC 复合体, 转录延伸 |

**主要研究方向**:
- MLL-AFF1 融合与急性淋巴细胞白血病 (ALL) (~60%)
- 超级延伸复合体 (SEC) 的组装与功能 (~20%)
- 转录延伸调控机制
- HIV Tat 介导的转录激活

**评价**: 134 篇论文 (narrow search)，在核蛋白中属于中等热度。绝大多数研究聚焦于其在白血病中的融合伙伴角色。AFF1 在正常发育中的独立功能、在非白血病组织中的调控角色、以及与染色质/表观遗传修饰的直接关系仍然研究不足，存在较大的挖掘空间。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 52.35 |
| PDB 实验结构 | — |
| 有序区域 (pLDDT>=70) 占比 | 22.6% |
| pLDDT>=90 占比 | 14.5% |
| pLDDT<50 占比 | 68.6% |
| 可用 PDB 条目 | 1个NMR片段 (2LM0, aa738-779) |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/AFF1/AFF1-PAE.png]]

**PAE 数值分析**:
- PAE 矩阵尺寸: 1210 x 1210
- PAE 总体均值: 27.72
- PAE <5 A 占比: 2.37%; <10 A 占比: 3.63%
- 对角线均值: 0.00

**评价**: AFF1 是高度无序蛋白，平均 pLDDT 仅 52.35，68.6% 的残基 pLDDT<50。仅 C 端 3 个小型高置信度区域: (962-1008), (1012-1084), (1131-1208) ——这些对应 AF4/FMR2 C-terminal homology domain。PAE 均值 27.72 非常高，仅 2.37% 的残基对 PAE<5 A，说明蛋白整体为高度柔性的伸展构象。UniProt收录1个NMR片段(2LM0, aa738-779)，覆盖极小(3.5%)。PubMed 134篇(≥100)，按非新颖蛋白标准，AlphaFold差+大量无序→评3分。这是固有无序蛋白 (IDP) 的典型特征，结构解析具有挑战性，但 IDP 的 scaffold 功能本身就是重要研究方向。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| InterPro/Pfam | AF4/FMR2 family (IPR007797); AF4 interaction motif (IPR043639/PF18875); AF4/FMR2 C-terminal homology domain (IPR043640/PF18876) |
| UniProt | 大量 disordered regions (1-45, 73-314, 366-957); 无经典 domain 注释 |
| GO (Component) | Super elongation complex; transcription elongation factor complex |
| GO (Process) | Regulation of gene expression |

**染色质调控潜力分析**: AFF1 是 SEC (超级延伸复合体) 的核心支架蛋白，直接参与 RNA Pol II 的转录延伸调控——这是染色质水平的核心调控事件。AF4/FMR2 C-terminal homology domain (CHD) 是转录延伸因子家族的保守特征域，AF4 interaction motif 介导与 P-TEFb 复合体的相互作用。虽然不是经典 chromatin-binding domain (如 bromodomain, chromodomain)，但其功能本质就是染色质/转录调控。蛋白的 IDR 区域可能介导液-液相分离 (LLPS)，在转录凝聚体 (transcriptional condensates) 形成中发挥作用。

#### 3.6 PPI Top partners:
| Partner | Score | 功能类别 | 与调控相关？ |
|---|---|---|---|
| ELL2 | 0.999 | SEC member, elongation factor | **Yes** |
| MLLT1 (ENL) | 0.999 | SEC member, YEATS domain reader | **Yes** |
| ELL | 0.999 | SEC member, elongation factor | **Yes** |
| CCNT1 (Cyclin T1) | 0.999 | P-TEFb subunit | **Yes** |
| CCNT2 (Cyclin T2) | 0.999 | P-TEFb subunit | **Yes** |
| CDK9 | 0.999 | P-TEFb kinase | **Yes** |
| AFF4 | 0.999 | SEC member, paralog | **Yes** |
| MLLT3 (AF9) | 0.999 | SEC member | **Yes** |
| EAF1 | 0.997 | SEC member | **Yes** |
| EAF2 | 0.989 | SEC member | **Yes** |
| ELL3 | 0.998 | SEC member, elongation factor | **Yes** |
| PAF1 | 0.999 | PAF1 complex, transcription | **Yes** |
| SUPT4H1 | 0.999 | DSIF complex, elongation | **Yes** |
| MLLT10 (AF10) | 0.999 | DOT1L recruiter | **Yes** |
| KMT2A (MLL) | 0.990 | Histone methyltransferase (H3K4) | **Yes** |
| DOT1L | 0.951 | Histone methyltransferase (H3K79) | **Yes** |
| LEO1 | 0.999 | PAF1 complex | **Yes** |
| CTR9 | 0.999 | PAF1 complex | **Yes** |
| CDC73 | 0.999 | PAF1 complex | **Yes** |
| ICE1/ICE2 | 0.998 | SEC-associated | **Yes** |

**UniProt 实验互作**: SEC 复合体 (EAF1, EAF2, CDK9, MLLT3/AF9, AFF1/AFF4, P-TEFb, ELL/ELL2/ELL3)

**PPI 互证**:
- 无法获取 humanPPI 数据 - STRING 和 UniProt 均确认 SEC 组分互作
- Top 10 overlap: N/A (单数据库)

**调控相关比例**: >95% (几乎所有 partners 均为转录/表观调控相关)

**评价**: PPI 和 DOT1L (H3K79 methyltransferase) 直接互作，表明其在表观遗传调控中也扮演重要角色。这是非常理想的染色质调控蛋白 PPI 特征。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 三维结构 | AlphaFold pLDDT + PDB | 无实验结构; AF 预测为 IDP | N/A |
| 结构域 | UniProt / InterPro / Pfam | AF4/FMR2 family + AF4_int + CHD 一致 | 一致 |
| PPI | STRING | SEC/PAF1/elongation + GO (SEC, transcription elongation complex) + Protein Atlas (nucleoplasm, Approved) → **+0.5**

- 结构域互证: InterPro + Pfam 均确认 AF4/FMR2 CHD → **+0.5**
 - 域功能与染色质转录调控一致 (SEC 功能)
- 三维结构: 无 PDB 实验结构 → 0
- PPI 互证: 无法获取 humanPPI → 0
- 进化保守性: AF4/FMR2 家族在脊椎动物中高度保守 → 未验证

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: 4/5 (强烈推荐作为转录调控/染色质研究方向候选)

**核心优势**:
1. 严格的核定位，作为 SEC 核心支架直接参与转录延伸调控
2. PPI , SEC, PAF1, DSIF 等核心转录机器，并与 KMT2A 和 DOT1L 等组蛋白修饰酶互作
3. 高度新颖性 (134 篇论文)，且研究集中于白血病融合，其正常组织功能和独立调控角色仍有大片空白
4. IDP 特征暗示液-液相分离 (LLPS) 和转录凝聚体形成的可能性——这是当前转录调控的热点方向

**风险/不确定性**:
1. 蛋白 ~69% 无序，结构解析极其困难，不适合传统的结晶学/X-ray/NMR 研究
2. IDP 的生化操作 (表达、纯化、活性测定) 具有挑战性
3. 作为 MLL 融合伙伴，已有大量的白血病领域研究，需要在正常生物学功能上做出差异化
4. 结构域非经典染色质域，可能需要在功能验证上投入更多精力

**下一步建议**:
- [ ] 重点研究方向: AFF1 在非白血病组织中 SEC 组装的特异性调控
- [ ] 利用 IDP 特征，探索 LLPS 和转录凝聚体形成
- [ ] 关注 AFF1 与 KMT2A/DOT1L 的互作如何协调转录延伸与组蛋白修饰
- [ ] 考虑冷冻电镜 (cryo-EM) 研究 SEC 全复合体结构 (而非单独 AFF1)

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51825
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172493-AFF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22AFF1%22 (E-utils API)
- STRING: https://string-db.org (API)
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/P51825/ (API)
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51825
- - humanPPI: 无法访问

![[Projects/TEreg-finding/protein-interested/detail/rejected/AFF1/AFF1-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/AFF1/AFF1-PAE.png]]




